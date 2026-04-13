<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aide Mutuelle - Le Réseau Social Solidaire</title>
    <style>
        :root { --vert-mutuelle: #2ecc71; --bleu-social: #3498db; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; margin: 0; text-align: center; color: #333; }
        .header { background: var(--vert-mutuelle); color: white; padding: 25px; font-size: 26px; font-weight: bold; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        
        /* Phrases Motivantes */
        .social-banner { background: #fff; padding: 15px; border-bottom: 3px solid var(--bleu-social); margin-bottom: 20px; }
        .motto { font-weight: bold; color: var(--bleu-social); font-size: 18px; display: block; }
        .sub-motto { font-size: 14px; color: #666; margin-top: 5px; }

        .container { padding: 15px; max-width: 500px; margin: auto; }
        .pack-card { background: white; border-radius: 20px; padding: 20px; margin-bottom: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: 0.3s; }
        .pack-card:active { transform: scale(0.98); }
        
        .btn { background: var(--vert-mutuelle); color: white; padding: 12px 25px; border: none; border-radius: 50px; cursor: pointer; font-size: 16px; font-weight: bold; width: 100%; margin-top: 10px; }
        .btn-parrain { background: var(--bleu-social); margin-top: 15px; }

        /* Section Progression & Parrainage */
        .progress-box { background: white; border-radius: 20px; padding: 20px; margin-top: 20px; display: none; }
        .bar-bg { background: #e0e0e0; border-radius: 10px; height: 25px; margin: 15px 0; overflow: hidden; }
        .bar-fill { background: linear-gradient(90deg, #2ecc71, #27ae60); width: 0%; height: 100%; transition: 1s; }
        
        .parrainage-info { background: #e8f4fd; padding: 15px; border-radius: 15px; margin-top: 15px; border: 1px dashed var(--bleu-social); }
        .code-display { font-size: 22px; font-weight: bold; color: var(--bleu-social); letter-spacing: 2px; }
    </style>
</head>
<body>

<div class="header">AIDE MUTUELLE 🌍</div>

<div class="social-banner">
    <span class="motto">"L'entraide 2.0 : Ensemble, on finance nos projets."</span>
    <div class="sub-motto">Le réseau social qui fait grandir ton argent.</div>
</div>

<div class="container">
    <div id="setup">
        <div class="pack-card">
            <h3>Pack Bronze - 2 000 F</h3>
            <p>Reçois 1 500 F (x2)</p>
            <button class="btn" onclick="choisirPack(2000, 1500)">Activer le Pack</button>
        </div>
        <div class="pack-card">
            <h3>Pack Argent - 5 000 F</h3>
            <p>Reçois 4 000 F (x2)</p>
            <button class="btn" onclick="choisirPack(5000, 4000)">Activer le Pack</button>
        </div>
        <div class="pack-card">
            <h3>Pack Or - 10 000 F</h3>
            <p>Reçois 8 000 F (x2)</p>
            <button class="btn" onclick="choisirPack(10000, 8000)">Activer le Pack</button>
        </div>
        <p style="font-size: 13px; color: #888;">Frais de gaz (20%) inclus pour la pérennité du réseau.</p>
    </div>

    <div id="espace-membre" style="display:none;">
        <div class="pack-card">
            <h2 id="msg-statut">File d'attente...</h2>
            <p id="phrase-motivante">"Fais un don, reçois le double. C'est la loi du réseau."</p>
            
            <div class="bar-bg"><div class="bar-fill" id="barre"></div></div>
            <p id="compteur-jours">Attente du couplage par le robot</p>
        </div>

        <div class="parrainage-info">
            <strong>TON CODE DE PARRAINAGE :</strong><br>
            <span class="code-display" id="mon-code">MUT-772</span><br>
            <p style="font-size: 14px;">🚀 <strong>Gagne du temps :</strong><br>Parraine un proche = 1 jour de gagné !</p>
            <button class="btn btn-parrain" onclick="simulerParrainage()">Parrainer un ami</button>
        </div>

        <button id="btn-retrait" class="btn" style="display:none; background: #f1c40f;" onclick="validerRetrait()">Prendre mon Gain</button>
    </div>
</div>

<script>
    let joursAttente = 14;
    let gainActuel = 0;

    function choisirPack(prix, gain) {
        gainActuel = gain;
        document.getElementById('setup').style.display = 'none';
        document.getElementById('espace-membre').style.display = 'block';
        alert("Enregistré ! Envoie ta capture au +227 89 06 28 06");
        
        // Simulation couplage après 3 secondes
        setTimeout(() => {
            alert("🎺 FANFARE ! Tu es couplé ! Ton cycle commence.");
            document.getElementById('msg-statut').innerText = "Argent en cours de travail...";
            document.getElementById('phrase-motivante').innerText = "Le réseau te propulse... Ton tour arrive !";
            actualiserProgression();
        }, 3000);
    }

    function actualiserProgression() {
        let pourcentage = ((14 - joursAttente) / 14) * 100;
        document.getElementById('barre').style.width = pourcentage + "%";
        document.getElementById('compteur-jours').innerText = "Plus que " + joursAttente + " jours avant ton retrait.";
        
        if (joursAttente <= 0) {
            document.getElementById('btn-retrait').style.display = 'block';
            document.getElementById('compteur-jours').innerText = "Ton gain de " + gainActuel + " F est prêt !";
        }
    }

    function simulerParrainage() {
        if (joursAttente > 0) {
            joursAttente -= 1; // On réduit d'un jour
            alert("Bravo ! +1 parrainage = -24h d'attente.");
            actualiserProgression();
        }
    }

    function validerRetrait() {
        let code = prompt("ADMIN (Lulu) : Entre ton code secret Airtel Money pour libérer les " + gainActuel + " F :");
        if (code) {
            alert("Paiement envoyé au membre ! Le robot réinjecte le capital pour le suivant.");
            joursAttente = 14; // On repart pour le 2ème cycle
            document.getElementById('btn-retrait').style.display = 'none';
            actualiserProgression();
        }
    }
</script>

</body>
</html>