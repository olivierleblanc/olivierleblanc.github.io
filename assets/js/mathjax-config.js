window.MathJax = {
  tex: {
    macros: {
      im: "\\mathrm{i}",
      bs: ["\\boldsymbol{#1}", 1], 
      Rbb: "\\mathbb{R}",
      Cbb: "\\mathbb{C}",
      cl: ["\\mathcal{#1}", 1],
      tinv: ["\\frac{1}{#1}", 1],
      rm: ["\\mathrm{#1}", 1],
      llbracket: "⟦",  // Unicode Left Double Bracket
      rrbracket: "⟧",   // Unicode Right Double Bracket
      upto: ["\\llbracket #1 \\rrbracket", 1],
      norm: ["#1\\lVert#2#1\\rVert_{#3}", 3],
      diag: "\\text{diag}",
      scp: ["#1\\langle #2, #3 #1\\rangle", 3], // scalar product
      modulo: ["{/#1/}_{#2}", 2],
    }
  }
};