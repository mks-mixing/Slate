#!/usr/bin/env python3
"""Make the Windows fork English-first at build time.

Do translations by source replacement only. Do NOT mutate the live DOM: Slate's
PDF text editor uses contenteditable nodes and a global MutationObserver can
interfere with caret/selection/edit state.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "src-tauri" / "frontend-dist" / "index.html"
APP = ROOT / "src-tauri" / "frontend-dist" / "app.js"
MAIN = ROOT / "src-tauri" / "src" / "main.rs"

HTML_REPLACEMENTS = {
    # Default-app prompt
    "Définir Slate comme lecteur PDF par défaut ?": "Set Slate as your default PDF reader?",
    "Tes fichiers PDF s'ouvriront directement dans Slate d'un double-clic.": "Your PDF files will open directly in Slate when you double-click them.",
    "Ne plus demander": "Don't ask again",
    "Plus tard": "Later",
    "Oui, définir par défaut": "Yes, set as default",

    # Main chrome / toolbars
    "Enregistrement automatique de ce document": "Automatically save this document",
    "Ouvrez un PDF, déposez-le ici, ou reprenez un fichier récent.": "Open a PDF, drop it here, or resume a recent file.",
    "Glissez un PDF ici, ou cliquez pour choisir": "Drop a PDF here, or click to choose",
    "Crée des documents exceptionnels avec Alto Express, inclus dans votre abonnement.": "Create exceptional documents with Alto Express, included with your subscription.",
    "Utiliser les outils de conception": "Use design tools",
    "Ajouter des repères d’impression": "Add printer marks",
    "Enregistrer au format PDF/X": "Save as PDF/X",
    "Définir des zones de page": "Set page boxes",
    "Concevoir une nouvelle page": "Design a new page",
    "En-tête et pied de page": "Header and footer",
    "Mettre le texte en forme": "Format text",
    "Rechercher une police…": "Search fonts…",
    "Sélectionne un bloc sur la page...": "Select a block on the page...",
    "Convertir les couleurs": "Convert colors",
    "Utiliser le prépresse": "Use prepress",
    "Aperçu de la sortie": "Output preview",
    "Contrôle en amont": "Preflight",
    "Gestionnaires d’encres": "Ink Manager",
    "Modifier la page": "Modify page",
    "Organiser les pages": "Organize pages",
    "Ajouter un contenu": "Add content",
    "Numéros de page": "Page numbers",
    "Police du document": "Document font",
    "Couleur du texte": "Text color",
    "Aligner à gauche": "Align left",
    "Aligner à droite": "Align right",
    "Liste à puces": "Bulleted list",
    "Liste numérotée": "Numbered list",
    "Texte sélectionné": "Selected text",
    "Concevoir avec Alto": "Design with Alto",
    "Styliser ce PDF": "Style this PDF",
    "Autres options": "Other options",
    "Combiner des fichiers": "Combine files",
    "Préparer un formulaire": "Prepare form",
    "Biffer un PDF": "Redact PDF",
    "Ouvrir un PDF": "Open a PDF",
    "Quitter Modifier": "Exit Modify",
    "Enregistrer la signature": "Save signature",
    "Créer une signature": "Create a signature",
    "Dessiner": "Draw",
    "Importer": "Upload",
    "Effacer": "Clear",
    "Signature": "Signature",
    "Initiales": "Initials",
    "Assistant IA": "AI Assistant",
    "Enreg. auto": "Auto-save",
    "Rétablir": "Redo",
    "Annuler": "Undo",
    "Imprimer": "Print",
    "Enregistrer": "Save",
    "Partager": "Share",
    "Historique": "History",
    "Modifier": "Modify",
    "Accueil": "Home",
    "Profil": "Profile",
    "Créer": "Create",
    "Retour": "Back",
    "Bientôt": "Coming soon",
    "Sélectionner": "Select",
    "Rotation": "Rotate",
    "Supprimer": "Delete",
    "Extraire": "Extract",
    "Filigrane": "Watermark",
    "Gras": "Bold",
    "Italique": "Italic",
    "Souligné": "Underline",
    "Alignement": "Alignment",
    "Centrer": "Center",
    "Listes": "Lists",
    "Inclinaison": "Rotation",
    "Appliquer": "Apply",
    "Masquer": "Hide",
    "Bonjour": "Hello",
    "Récents": "Recent",
    "Affichage": "View",
    "Grille": "Grid",
    "Liste": "List",
    "Texte": "Text",
    "Image": "Image",
    "Plus": "More",
}

RUST_REPLACEMENTS = {
    # App menu
    "À propos des modules externes Slate...": "About Slate External Modules...",
    "À propos de Slate": "About Slate",
    "Préférences...": "Preferences...",
    "Assistant de configuration d’accessibilité...": "Accessibility Setup Assistant...",
    "Aucun service disponible": "No services available",
    "Masquer les autres": "Hide Others",
    "Masquer Slate": "Hide Slate",
    "Afficher tout": "Show All",
    "Quitter Slate": "Quit Slate",

    # File menu
    "Ouvrir les fichiers récents": "Open Recent Files",
    "Tous les fichiers récents...": "All Recent Files...",
    "Créer une page vierge": "Create Blank Page",
    "Créer un PDF": "Create PDF",
    "Enregistrer sous un autre": "Save as Other",
    "PDF modifié...": "Modified PDF...",
    "PDF modifié": "Modified PDF",
    "Exporter un PDF": "Export PDF",
    "Combiner les fichiers": "Combine Files",
    "Enregistrer sous...": "Save As...",
    "Compresser un fichier PDF": "Compress PDF",
    "Protéger à l’aide d’un mot de passe": "Protect with Password",
    "Demander des signatures électroniques": "Request Electronic Signatures",
    "Partager le fichier": "Share File",
    "Recherche avancée": "Advanced Search",
    "Propriétés du document...": "Document Properties...",
    "Fermer le fichier": "Close File",

    # Edit menu
    "Ajouter une image": "Add Image",
    "Depuis un fichier...": "From File...",
    "Ajouter une signature": "Add Signature",
    "Modifier le PDF": "Modify PDF",
    "Ajouter du texte": "Add Text",
    "Supprimer la page": "Delete Page",
    "Faire pivoter la page (horaire)": "Rotate Page Clockwise",
    "Faire pivoter la page (antihoraire)": "Rotate Page Counterclockwise",
    "Organiser les pages": "Organize Pages",
    "Préparer le formulaire": "Prepare Form",
    "Ajouter un mot de passe": "Add Password",
    "Caractères spéciaux...": "Special Characters...",
    "Tout sélectionner": "Select All",
    "Couper": "Cut",
    "Copier": "Copy",
    "Coller": "Paste",

    # View menu
    "Faire pivoter la vue": "Rotate View",
    "Navigation de pages": "Page Navigation",
    "Page précédente": "Previous Page",
    "Page suivante": "Next Page",
    "Panneaux latéraux": "Side Panels",
    "Largeur page": "Page Width",
    "Zoom avant": "Zoom In",
    "Zoom arrière": "Zoom Out",
    "Afficher/Masquer": "Show/Hide",
    "Barre d’outils droite": "Right Toolbar",
    "Thème d’affichage": "Display Theme",
    "Lecture audio": "Read Aloud",
    "Lire à voix haute": "Read Aloud",
    "Ouvrir le panneau prépresse": "Open Prepress Panel",
    "Mode Lecture": "Reading Mode",
    "Mode plein écran": "Full Screen Mode",
    "Désactiver la nouvelle version d’Acrobat": "Disable New Acrobat",
    "Dispositif de suivi...": "Tracking Device...",

    # Window menu
    "Déplacer et redimensionner": "Move and Resize",
    "Vers la gauche": "To the Left",
    "Vers la droite": "To the Right",
    "Mosaïque": "Tile",
    "Horizontale": "Horizontal",
    "Verticale": "Vertical",
    "Déplacer vers l’écran principal": "Move to Main Display",
    "Nouvelle fenêtre": "New Window",
    "Réduire": "Minimize",

    # Help / generic
    "Comment utiliser l’Assistant IA": "How to Use the AI Assistant",
    "Aide “Modifier un PDF”": "Modify PDF Help",
    "Aide Slate": "Slate Help",
    "Tutoriels Slate": "Slate Tutorials",
    "Gérer mon compte...": "Manage My Account...",
    "Rechercher les mises à jour": "Check for Updates",
    "Utiliser le prépresse": "Use Prepress",
    "Convertir les couleurs…": "Convert Colors…",
    "Biffer un PDF": "Redact PDF",
    "Scan et OCR": "Scan and OCR",
    "Protection": "Protection",
    "Antihoraire": "Counterclockwise",
    "Horaire": "Clockwise",
    "Tous les outils": "All Tools",
    "Système": "System",
    "Clair": "Light",
    "Remplir": "Fill",
    "Centrer": "Center",
    "Cascade": "Cascade",
    "Rechercher": "Search",
    "Affichage": "View",
    "Fenêtre": "Window",
    "Édition": "Edit",
    "Fichier": "File",
    "Aide": "Help",
    "Ouvrir...": "Open...",
    "Imprimer...": "Print...",
    "Enregistrer": "Save",
    "Créer": "Create",
}

# Keep automatic language selection English in this fork. Explicit French is
# still respected if the user deliberately chooses it in Settings.
APP_REPLACEMENTS = {
    "return navigator.language?.toLowerCase().startsWith('fr') ? 'fr' : 'en';": "return 'en';",
}


def replace_many(text: str, replacements: dict[str, str]) -> tuple[str, int]:
    changed = 0
    for source in sorted(replacements, key=len, reverse=True):
        target = replacements[source]
        count = text.count(source)
        if count:
            text = text.replace(source, target)
            changed += count
    return text, changed


def patch(path: Path, replacements: dict[str, str]) -> int:
    original = path.read_text(encoding="utf-8")
    patched, count = replace_many(original, replacements)
    if patched != original:
        path.write_text(patched, encoding="utf-8", newline="\n")
    return count


def main() -> None:
    html_count = patch(INDEX, HTML_REPLACEMENTS)
    rust_count = patch(MAIN, RUST_REPLACEMENTS)
    app_count = patch(APP, APP_REPLACEMENTS)
    print(
        f"English localization: {html_count} HTML replacements, "
        f"{rust_count} native-menu replacements, {app_count} app replacements. "
        "No runtime DOM observer installed."
    )


if __name__ == "__main__":
    main()
