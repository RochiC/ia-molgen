export default function handler(req, res) {
  const url = new URL(req.url, `http://${req.headers.host}`);
  const target = (url.searchParams.get("target") || "SGLT2").toUpperCase();
  const n = Math.min(parseInt(url.searchParams.get("n") || "10", 10), 50);

  const SAMPLES = {
    SGLT2: ["C(C(=O)O)N","CC(=O)O","CCO","C1=CC=CC=C1","CCN(CC)CC","CCOC(=O)C","CNC(=O)C","CC(C)O","COC","CCC(=O)O"],
    GLP1R: ["CC(C)OC(=O)N1CCC(CC1)C2=CC=CC=C2","CCN(CC)CCOC(=O)C1=CC=CC=C1","COC1=CC=CC=C1O","CC(C)CC1=CC=CC=C1","CCOC(=O)NCC","CN(C)C(=O)C","CC(C)C(=O)O","CC(C)N","COCCN","CC(C)CO"]
  };
  const pool = SAMPLES[target] || SAMPLES.SGLT2;
  const smiles = Array.from({length:n}, () => pool[Math.floor(Math.random()*pool.length)]);

  res.setHeader("Access-Control-Allow-Origin", "*");
  res.status(200).json({ target, count: smiles.length, smiles });
}
