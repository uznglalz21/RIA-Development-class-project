function init() {
    const path = window.location.pathname;
    const btn = document.querySelector(".btn");
  
    if (!btn) return;
  
    if (path.includes("index.html")) {
      setupEmailPage(btn);
    } else if (path.includes("q2.html")) {
      setupPalindromePage(btn);
    } else if (path.includes("q3.html")) {
      setupEncodingPage(btn);
    }
  }
  
  function setupEmailPage(button) {
    const emailP = document.getElementById("email");
    const nameP = document.getElementById("name");
    const domainP = document.getElementById("domain");
  
    const emailInput = document.createElement("input");
    emailInput.type = "text";
    emailInput.placeholder = "Enter email (e.g. user@example.com)";
    emailInput.id = "emailInput";
    emailP.replaceWith(emailInput);
  
    button.addEventListener("click", () => {
      const value = emailInput.value.trim();
      if (value.includes("@")) {
        const [name, domain] = value.split("@");
        nameP.textContent = `Your name is ${name}`;
        domainP.textContent = `Your domain is ${domain}`;
      } else {
        nameP.textContent = "Invalid email format.";
        domainP.textContent = "";
      }
    });
  }
  
  function setupPalindromePage(button) {
    const wordP = document.getElementById("word");
    const answer = document.querySelector(".answer");
  
    const wordInput = document.createElement("input");
    wordInput.type = "text";
    wordInput.placeholder = "Enter a word";
    wordInput.id = "wordInput";
    wordP.replaceWith(wordInput);
  
    button.addEventListener("click", () => {
      const value = wordInput.value.trim().toLowerCase();
      const reversed = value.split("").reverse().join("");
      if (value && value === reversed) {
        answer.textContent = `"${value}" is a palindrome.`;
        answer.className = "answer";
      } else {
        answer.textContent = `"${value}" is NOT a palindrome.`;
        answer.className = "response";
      }
    });
  }
  
  function setupEncodingPage(button) {
    const wordP = document.getElementById("word");
    const encodedP = document.getElementById("encoded");
  
    const encodeInput = document.createElement("input");
    encodeInput.type = "text";
    encodeInput.placeholder = "Enter a word (e.g. aaabbbcc)";
    encodeInput.id = "encodeInput";
    wordP.replaceWith(encodeInput);
  
    button.addEventListener("click", () => {
      const value = encodeInput.value.trim();
      if (!value) {
        encodedP.textContent = "Please enter a word.";
        return;
      }
  
      let result = "";
      let count = 1;
      for (let i = 0; i < value.length; i++) {
        if (value[i] === value[i + 1]) {
          count++;
        } else {
          result += value[i] + count;
          count = 1;
        }
      }
  
      encodedP.textContent = `Your encoded word is ${result}`;
    });
  }
  
  init();
  