UPDATE profile SET
  name = 'Harshini Maryada',
  email = 'maryada.harshini.22031@iitgoa.ac.in',
  education = 'B.Tech. in Computer Science and Engineering, IIT Goa (CGPA: 6.11/10)',
  skills = json('["C","C++","Python","Data Structures","Algorithms","HTML","CSS","JavaScript","AutoCAD","LaTeX","Linux","Git","GitHub","VSCode","AI","ML","Probability","Statistics","Computer Networks","Operating Systems","Digital Systems Design","Coding Theory","Cryptography"]'),
  work = json('["Coding club contributor – coding challenges, peer reviews"]'),
  projects = json('[' ||
    '{"title":"TCP Congestion Control Simulation","description":"Simulated TCP congestion control algorithms in Python; analyzed performance metrics.","links":["https://github.com/HarshiniMaryada/TCP-Congestion-Control"]},' ||
    '{"title":"Calculator Web App","description":"Responsive calculator with custom evaluator, keyboard support; hosted on GitHub Pages.","links":["https://harshinimaryada.github.io/Calculator-app/"]},' ||
    '{"title":"Goldwasser–Micali Research","description":"Research on probabilistic encryption and semantic security; potential IoT applications.","links":["https://github.com/HarshiniMaryada"]}' ||
  ']'),
  links = json('{"github":"https://github.com/HarshiniMaryada","linkedin":"https://www.linkedin.com/in/maryada-harshini-a75995298","naukri":"https://www.naukri.com/code360/profile/HarshiniYadav"}'),
  updated_at = CURRENT_TIMESTAMP
WHERE id = 1;
