/**
 * ============================================================================
 * Modern Calculator Web Application
 * Vanilla JavaScript (ES6+) Implementation
 * ============================================================================
 */
// Encapsulate Calculator logic in a clean, stateful Class
class Calculator {
    constructor(previousOperandTextElement, currentOperandTextElement, displayContainer) {
        this.previousOperandTextElement = previousOperandTextElement;
        this.currentOperandTextElement = currentOperandTextElement;
        this.displayContainer = displayContainer;

        // Calculation History Array
        this.history = JSON.parse(localStorage.getItem("calc_history")) || [];

        // Reset state to initial values
        this.clear();
    }
    /**
     * Resets all calculation states to initial defaults (AC)
     */
    clear() {
        this.currentOperand = "0";
        this.previousOperand = "";
        this.operation = undefined;
        this.isErrorState = false;
        this.shouldResetScreen = false;
        this.updateDisplay();
    }
    /**
     * Deletes the last character from the current input (DEL)
     */
    delete() {
        if (this.isErrorState) {
            this.clear();
            return;
        }
        if (this.shouldResetScreen) {
            return;
        }
        // If only one digit left or negative single digit, reset to 0
        if (this.currentOperand.length === 1 || (this.currentOperand.length === 2 && this.currentOperand.startsWith("-"))) {
            this.currentOperand = "0";
        } else {
            this.currentOperand = this.currentOperand.slice(0, -1);
        }
        this.updateDisplay();
    }
    /**
     * Appends a number or digit to the current display
     */
    appendNumber(number) {
        // If in error state or freshly evaluated, start a new calculation
        if (this.isErrorState || this.shouldResetScreen) {
            this.currentOperand = "";
            this.shouldResetScreen = false;
            this.isErrorState = false;
        }
        // If starting from initial 0 and a non-zero is typed, replace it
        if (this.currentOperand === "0" && number !== ".") {
            this.currentOperand = number;
        } else {
            // Prevent multiple zero prefixes (e.g. "00")
            if (this.currentOperand === "0" && number === "0") return;
            this.currentOperand += number;
        }
        this.updateDisplay();
    }
    /**
     * Appends decimal point, ensuring only one decimal exists in a number
     */
    appendDecimal() {
        if (this.isErrorState || this.shouldResetScreen) {
            this.currentOperand = "0";
            this.shouldResetScreen = false;
            this.isErrorState = false;
        }
        if (this.currentOperand.includes(".")) {
            this.triggerShake();
            return;
        }
        if (this.currentOperand === "") {
            this.currentOperand = "0";
        }
        this.currentOperand += ".";
        this.updateDisplay();
    }
    /**
     * Inverts the sign of the current number (+/-)
     */
    negate() {
        if (this.isErrorState) return;
        if (this.currentOperand === "0" || this.currentOperand === "") return;
        if (this.currentOperand.startsWith("-")) {
            this.currentOperand = this.currentOperand.substring(1);
        } else {
            this.currentOperand = "-" + this.currentOperand;
        }
        this.updateDisplay();
    }
    /**
     * Calculates percentage (%)
     */
    applyPercent() {
        if (this.isErrorState || this.currentOperand === "") return;
        const current = parseFloat(this.currentOperand);
        if (isNaN(current)) return;
        let result;
        if (this.previousOperand !== "" && this.operation) {
            const prev = parseFloat(this.previousOperand);
            // For addition or subtraction: e.g. 200 + 10% = 200 + 20
            if (this.operation === "+" || this.operation === "-") {
                result = (prev * current) / 100;
            } else {
                // For multiplication or division: e.g. 50 * 10% = 50 * 0.1
                result = current / 100;
            }
        } else {
            result = current / 100;
        }
        this.currentOperand = this.formatNumber(result).toString();
        this.updateDisplay();
    }
    /**
     * Chooses an arithmetic operation (+, -, *, /)
     */
    chooseOperation(operation) {
        if (this.isErrorState) return;
        // Allow user to switch operator if they haven't typed the next number yet
        if (this.currentOperand === "" && this.previousOperand !== "") {
            this.operation = operation;
            this.updateDisplay();
            return;
        }
        // If there is already a previous operand, compute it first (chained math)
        if (this.previousOperand !== "") {
            const computeSuccess = this.compute();
            if (!computeSuccess) return; // Stopped due to error (e.g., divide by zero)
        }
        this.operation = operation;
        this.previousOperand = this.currentOperand;
        this.currentOperand = "";
        this.updateDisplay();
    }
    /**
     * Performs the mathematical calculation
     * @returns {boolean} true if successful, false on error
     */
    compute() {
        const prev = parseFloat(this.previousOperand);
        const current = parseFloat(this.currentOperand);
        // If either operand is invalid, do nothing
        if (isNaN(prev) || isNaN(current) || !this.operation) {
            return false;
        }
        let computation;
        switch (this.operation) {
            case "+":
                computation = prev + current;
                break;
            case "-":
                computation = prev - current;
                break;
            case "*":
                computation = prev * current;
                break;
            case "/":
                // Prevent division by zero
                if (current === 0) {
                    this.showError("Cannot divide by zero");
                    return false;
                }
                computation = prev / current;
                break;
            default:
                return false;
        }
        // Fix floating point issues (e.g., 0.1 + 0.2 = 0.3)
        const formattedResult = this.formatNumber(computation);
        // Save to calculation history
        const expressionString = `${this.formatDisplayNumber(prev)} ${this.getOperatorSymbol(this.operation)} ${this.formatDisplayNumber(current)}`;
        this.saveHistory(expressionString, formattedResult.toString());
        // Update state
        this.currentOperand = formattedResult.toString();
        this.operation = undefined;
        this.previousOperand = "";
        this.shouldResetScreen = true;
        this.isErrorState = false;
        this.updateDisplay();
        return true;
    }
    /**
     * Handles division by zero or invalid operations gracefully
     */
    showError(message) {
        this.isErrorState = true;
        this.currentOperand = message;
        this.previousOperand = "";
        this.operation = undefined;
        this.shouldResetScreen = true;
        this.triggerShake();
        this.updateDisplay();
    }
    /**
     * Shakes the display container on invalid inputs or errors
     */
    triggerShake() {
        this.displayContainer.classList.remove("shake");
        void this.displayContainer.offsetWidth; // Trigger DOM reflow
        this.displayContainer.classList.add("shake");
        setTimeout(() => {
            this.displayContainer.classList.remove("shake");
        }, 400);
    }
    /**
     * Fixes JavaScript floating point precision issues
     */
    formatNumber(num) {
        if (isNaN(num)) return 0;
        return Math.round((num + Number.EPSILON) * 1e12) / 1e12;
    }
    /**
     * Formats numbers with localized grouping commas (e.g., 1,234.56)
     */
    formatDisplayNumber(number) {
        if (this.isErrorState) return number;
        const stringNumber = number.toString();
        const integerDigits = parseFloat(stringNumber.split(".")[0]);
        const decimalDigits = stringNumber.split(".")[1];
        let integerDisplay;
        if (isNaN(integerDigits)) {
            integerDisplay = stringNumber.startsWith("-") ? "-" : "";
        } else {
            integerDisplay = integerDigits.toLocaleString("en-US", {
                maximumFractionDigits: 0,
            });
        }
        if (decimalDigits != null) {
            return `${integerDisplay}.${decimalDigits}`;
        } else {
            return integerDisplay;
        }
    }
    /**
     * Returns math symbol corresponding to internal operator
     */
    getOperatorSymbol(op) {
        switch (op) {
            case "+": return "+";
            case "-": return "−";
            case "*": return "×";
            case "/": return "÷";
            default: return "";
        }
    }
    /**
     * Refreshes the display screen numbers and active operator styles
     */
    updateDisplay() {
        if (this.isErrorState) {
            this.currentOperandTextElement.textContent = this.currentOperand;
            this.currentOperandTextElement.classList.add("error-state");
            this.previousOperandTextElement.textContent = "";
            return;
        }
        this.currentOperandTextElement.classList.remove("error-state");
        // Display current number with formatting
        if (this.currentOperand === "") {
            this.currentOperandTextElement.textContent = "0";
        } else {
            this.currentOperandTextElement.textContent = this.formatDisplayNumber(this.currentOperand);
        }
        // Display upper previous operand and pending operator
        if (this.operation != null && this.previousOperand !== "") {
            this.previousOperandTextElement.textContent =
                `${this.formatDisplayNumber(this.previousOperand)} ${this.getOperatorSymbol(this.operation)}`;
        } else {
            this.previousOperandTextElement.textContent = "";
        }
        // Dynamically adjust font size if number is very long
        this.adjustFontSize();
        // Highlight active operator button
        document.querySelectorAll(".btn-operator").forEach(btn => {
            if (this.operation && btn.getAttribute("data-operator") === this.operation && this.currentOperand === "") {
                btn.classList.add("operator-active");
            } else {
                btn.classList.remove("operator-active");
            }
        });
    }
    /**
     * Adjusts the font size dynamically so long numbers do not overflow
     */
    adjustFontSize() {
        const length = this.currentOperandTextElement.textContent.length;
        if (length > 15) {
            this.currentOperandTextElement.style.fontSize = "1.3rem";
        } else if (length > 11) {
            this.currentOperandTextElement.style.fontSize = "1.7rem";
        } else if (length > 8) {
            this.currentOperandTextElement.style.fontSize = "2rem";
        } else {
            this.currentOperandTextElement.style.fontSize = "2.3rem";
        }
    }
    /**
     * Records a calculation into history array and updates storage
     */
    saveHistory(expression, result) {
        const item = {
            id: Date.now(),
            expression: expression,
            result: result
        };
        this.history.unshift(item);
        if (this.history.length > 25) {
            this.history.pop();
        }
        localStorage.setItem("calc_history", JSON.stringify(this.history));
        renderHistoryList(this.history);
    }
    /**
     * Clears calculation history
     */
    clearHistory() {
        this.history = [];
        localStorage.removeItem("calc_history");
        renderHistoryList(this.history);
    }
    /**
     * Recalls a value from history into current operand
     */
    recallHistoryResult(val) {
        this.currentOperand = val.toString();
        this.shouldResetScreen = true;
        this.isErrorState = false;
        this.updateDisplay();
    }
}
/* ==========================================================================
   DOM Elements & Initialization
   ========================================================================== */
document.addEventListener("DOMContentLoaded", () => {
    const previousOperandTextElement = document.getElementById("previous-operand");
    const currentOperandTextElement = document.getElementById("current-operand");
    const displayContainer = document.querySelector(".display-container");
    // Create calculator instance
    const calculator = new Calculator(
        previousOperandTextElement,
        currentOperandTextElement,
        displayContainer
    );
    // Keypad Buttons
    const numberButtons = document.querySelectorAll("[data-number]");
    const operatorButtons = document.querySelectorAll("[data-operator]");
    const actionButtons = document.querySelectorAll("[data-action]");
    // UI Panels and Toggles
    const themeToggleBtn = document.getElementById("theme-toggle-btn");
    const historyToggleBtn = document.getElementById("history-toggle-btn");
    const historyPanel = document.getElementById("history-panel");
    const clearHistoryBtn = document.getElementById("clear-history-btn");
    // Initialize History List from storage
    renderHistoryList(calculator.history);
    /* --------------------------------------------------------------------------
       Button Click Event Listeners
       -------------------------------------------------------------------------- */
    // Number Buttons (0 - 9)
    numberButtons.forEach(button => {
        button.addEventListener("click", () => {
            calculator.appendNumber(button.getAttribute("data-number"));
        });
    });
    // Operator Buttons (+, -, *, /)
    operatorButtons.forEach(button => {
        button.addEventListener("click", () => {
            calculator.chooseOperation(button.getAttribute("data-operator"));
        });
    });
    // Action Buttons (AC, DEL, ., =, %, ±)
    actionButtons.forEach(button => {
        button.addEventListener("click", () => {
            const action = button.getAttribute("data-action");
            switch (action) {
                case "clear":
                    calculator.clear();
                    break;
                case "delete":
                    calculator.delete();
                    break;
                case "decimal":
                    calculator.appendDecimal();
                    break;
                case "percent":
                    calculator.applyPercent();
                    break;
                case "negate":
                    calculator.negate();
                    break;
                case "calculate":
                    calculator.compute();
                    break;
            }
        });
    });
    /* --------------------------------------------------------------------------
       Theme Switcher Logic (Dark / Light Theme)
       -------------------------------------------------------------------------- */
    const savedTheme = localStorage.getItem("calc_theme") || "dark";
    setTheme(savedTheme);
    themeToggleBtn.addEventListener("click", () => {
        const isDark = document.body.classList.contains("dark-theme");
        const nextTheme = isDark ? "light" : "dark";
        setTheme(nextTheme);
    });
    function setTheme(theme) {
        if (theme === "light") {
            document.body.classList.remove("dark-theme");
            document.body.classList.add("light-theme");
        } else {
            document.body.classList.remove("light-theme");
            document.body.classList.add("dark-theme");
        }
        localStorage.setItem("calc_theme", theme);
    }
    /* --------------------------------------------------------------------------
       History Drawer & Event Handlers
       -------------------------------------------------------------------------- */
    historyToggleBtn.addEventListener("click", () => {
        const isOpen = historyPanel.classList.toggle("active");
        historyPanel.setAttribute("aria-hidden", !isOpen);
    });
    // Close history drawer when clicking outside
    document.addEventListener("click", (e) => {
        if (!historyPanel.contains(e.target) && !historyToggleBtn.contains(e.target)) {
            historyPanel.classList.remove("active");
            historyPanel.setAttribute("aria-hidden", "true");
        }
    });
    clearHistoryBtn.addEventListener("click", () => {
        calculator.clearHistory();
    });
    // Clicking a history item restores that result to current calculation
    document.getElementById("history-list").addEventListener("click", (e) => {
        const item = e.target.closest(".history-item");
        if (!item) return;
        const result = item.getAttribute("data-result");
        if (result) {
            calculator.recallHistoryResult(result);
            historyPanel.classList.remove("active");
            historyPanel.setAttribute("aria-hidden", "true");
        }
    });
    /* --------------------------------------------------------------------------
       Keyboard Event Listeners & Visual Key Press Animation
       -------------------------------------------------------------------------- */
    window.addEventListener("keydown", (e) => {
        let key = e.key;
        // Prevent default browser behavior for calculator hotkeys
        if (["/", "*", "+", "-", "Enter", "Backspace", "Escape"].includes(key)) {
            e.preventDefault();
        }
        // Number keys (0 - 9)
        if (key >= "0" && key <= "9") {
            calculator.appendNumber(key);
            animateButton(`button[data-number="${key}"]`);
            return;
        }
        // Decimal point
        if (key === "." || key === ",") {
            calculator.appendDecimal();
            animateButton(`button[data-action="decimal"]`);
            return;
        }
        // Operators
        if (key === "+" || key === "-") {
            calculator.chooseOperation(key);
            animateButton(`button[data-operator="${key}"]`);
            return;
        }
        if (key === "*" || key === "x" || key === "X") {
            calculator.chooseOperation("*");
            animateButton(`button[data-operator="*"]`);
            return;
        }
        if (key === "/") {
            calculator.chooseOperation("/");
            animateButton(`button[data-operator="/"]`);
            return;
        }
        // Equals / Enter
        if (key === "Enter" || key === "=") {
            calculator.compute();
            animateButton(`button[data-action="calculate"]`);
            return;
        }
        // Delete (Backspace)
        if (key === "Backspace") {
            calculator.delete();
            animateButton(`button[data-action="delete"]`);
            return;
        }
        // Clear (Escape or Delete key)
        if (key === "Escape" || key === "Delete") {
            calculator.clear();
            animateButton(`button[data-action="clear"]`);
            return;
        }
        // Percentage (%)
        if (key === "%") {
            calculator.applyPercent();
            animateButton(`button[data-action="percent"]`);
            return;
        }
    });
    /**
     * Adds brief visual click/press animation to matching button on physical keypress
     */
    function animateButton(selector) {
        const btn = document.querySelector(selector);
        if (!btn) return;
        btn.classList.add("active-press");
        setTimeout(() => {
            btn.classList.remove("active-press");
        }, 150);
    }
});
/**
 * Renders history list items dynamically inside the history panel
 */
function renderHistoryList(history) {
    const historyListElement = document.getElementById("history-list");
    if (!historyListElement) return;
    if (!history || history.length === 0) {
        historyListElement.innerHTML = `<p class="history-empty">No calculations yet</p>`;
        return;
    }
    historyListElement.innerHTML = history.map(item => `
    <div class="history-item" data-result="${item.result}" title="Click to use ${item.result}">
      <span class="history-expression">${item.expression} =</span>
      <span class="history-result">${item.result}</span>
    </div>
  `).join("");
}