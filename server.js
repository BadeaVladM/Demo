const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.static('public'));

app.get('/api/values', (req, res) => {
  const soil = (30 + Math.random() * 50).toFixed(1);
  const ph = (5.5 + Math.random() * 8).toFixed(1);
  const temp = (20 + Math.random() * 35).toFixed(1);
  res.json({ soil, ph, temp });
});

app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
