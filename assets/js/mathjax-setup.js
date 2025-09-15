window.MathJax = {
  tex: {
    packages: { "[+]": ["ams"] }, // Explicitly include 'base' for basic commands
    tags: "ams",
    inlineMath: [
      ["$", "$"],
      ["\\(", "\\)"],
    ],
    macros: {
      llbracket: "{\\mathopen{\\lbrack\\kern-0.15em\\lbrack}}",
      rrbracket: "{\\mathclose{\\rbrack\\kern-0.15em\\rbrack}}",
    },
  },
  options: {
    renderActions: {
      addCss: [
        200,
        function (doc) {
          const style = document.createElement("style");
          style.innerHTML = `
          .mjx-container {
            color: inherit;
          }
        `;
          document.head.appendChild(style);
        },
        "",
      ],
    },
  },
};
