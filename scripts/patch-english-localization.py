#!/usr/bin/env python3
"""Normalize Slate's shipped UI to English without rewriting the large generated frontend by hand.

This fork is English-first. The upstream frontend currently contains a mixture of
English and French defaults, plus some dynamically-created French strings. This
script is intentionally idempotent and runs before the Windows build.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "src-tauri" / "frontend-dist" / "index.html"
APP = ROOT / "src-tauri" / "frontend-dist" / "app.js"
MAIN = ROOT / "src-tauri" / "src" / "main.rs"

# Static HTML defaults. Longer phrases are replaced first so shorter entries do
# not partially rewrite them.
HTML_REPLACEMENTS = {
    "Enregistrement automatique de ce document": "Automatically save this document",
    "Crée des documents exceptionnels avec Alto Express, inclus dans votre abonnement.": "Create exceptional documents with Alto Express, included with your subscription.",
    "Ouvrez un PDF, déposez-le ici, ou reprenez un fichier récent.": "Open a PDF, drop it here, or resume a recent file.",
    "Glissez un PDF ici, ou cliquez pour choisir": "Drop a PDF here, or click to choose",
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
    "Plus": "More",
}

# Native Tauri menu labels are currently hard-coded in French upstream. These
# replacements affect only the source strings used to build the desktop menus.
RUST_REPLACEMENTS = {
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
    "Déplacer et redimensionner": "Move and Resize",
    "Vers la gauche": "To the Left",
    "Vers la droite": "To the Right",
    "Mosaïque": "Tile",
    "Horizontale": "Horizontal",
    "Verticale": "Vertical",
    "Fenêtre": "Window",
    "Déplacer vers l’écran principal": "Move to Main Display",
    "Nouvelle fenêtre": "New Window",
    "Réduire": "Minimize",
    "Comment utiliser l’Assistant IA": "How to Use the AI Assistant",
    "Aide “Modifier un PDF”": "Modify PDF Help",
    "Aide Slate": "Slate Help",
    "Tutoriels Slate": "Slate Tutorials",
    "Gérer mon compte...": "Manage My Account...",
    "Rechercher les mises à jour": "Check for Updates",
    "Tout sélectionner": "Select All",
    "Édition": "Edit",
    "Couper": "Cut",
    "Copier": "Copy",
    "Coller": "Paste",
    "Protection": "Protection",
    "Antihoraire": "Counterclockwise",
    "Horaire": "Clockwise",
    "Tous les outils": "All Tools",
    "Utiliser le prépresse": "Use Prepress",
    "Convertir les couleurs…": "Convert Colors…",
    "Affichage": "View",
    "Système": "System",
    "Clair": "Light",
    "Remplir": "Fill",
    "Centrer": "Center",
    "Cascade": "Cascade",
    "Rechercher": "Search",
    "Aide": "Help",
    "Fichier": "File",
    "Ouvrir...": "Open...",
    "Imprimer...": "Print...",
    "Enregistrer": "Save",
    "Créer": "Create",
    "Biffer un PDF": "Redact PDF",
    "Scan et OCR": "Scan and OCR",
}

# Dynamic UI strings are not all wired to data-label-key. This helper reuses
# the existing en/fr translation dictionaries and catches untranslated text
# nodes/attributes created after startup as well.
JS_MARKER = "/* mks-english-localization-hotfix */"
JS_HELPER = r'''

/* mks-english-localization-hotfix */
(() => {
	const manual = new Map([
		['Accueil', 'Home'], ['Créer', 'Create'], ['Profil', 'Profile'],
		['Assistant IA', 'AI Assistant'], ['Annuler', 'Undo'], ['Rétablir', 'Redo'],
		['Imprimer', 'Print'], ['Enregistrer', 'Save'], ['Partager', 'Share'],
		['Modifier', 'Modify'], ['Historique', 'History'], ['Retour', 'Back'],
		['Bientôt', 'Coming soon'], ['Bonjour', 'Hello'], ['Récents', 'Recent'],
		['Affichage', 'View'], ['Grille', 'Grid'], ['Liste', 'List'],
		['Enreg. auto', 'Auto-save'], ['Utiliser le prépresse', 'Use prepress'],
		['Convertir les couleurs', 'Convert colors'], ['Modifier la page', 'Modify page'],
		['Ajouter un contenu', 'Add content'], ['Organiser les pages', 'Organize pages'],
		['En-tête et pied de page', 'Header and footer'], ['Filigrane', 'Watermark'],
		['Numéros de page', 'Page numbers'], ['Mettre le texte en forme', 'Format text'],
		['Police du document', 'Document font'], ['Rechercher une police…', 'Search fonts…'],
		['Texte sélectionné', 'Selected text'], ['Appliquer', 'Apply'], ['Masquer', 'Hide'],
		['Autres options', 'Other options'], ['Combiner des fichiers', 'Combine files'],
		['Biffer un PDF', 'Redact PDF'], ['Préparer un formulaire', 'Prepare form']
	]);

	function englishLookup() {
		const map = new Map(manual);
		if (typeof translations === 'object' && translations?.fr && translations?.en) {
			for (const [key, frValue] of Object.entries(translations.fr)) {
				const enValue = translations.en[key];
				if (typeof frValue === 'string' && typeof enValue === 'string' && frValue !== enValue) {
					map.set(frValue.trim(), enValue);
				}
			}
		}
		return map;
	}

	function translateTextNode(node, map) {
		if (!node?.nodeValue) return;
		const trimmed = node.nodeValue.trim();
		if (!trimmed) return;
		const translated = map.get(trimmed);
		if (!translated || translated === trimmed) return;
		const leading = node.nodeValue.match(/^\s*/)?.[0] || '';
		const trailing = node.nodeValue.match(/\s*$/)?.[0] || '';
		node.nodeValue = `${leading}${translated}${trailing}`;
	}

	function translateElement(element, map) {
		if (!(element instanceof Element)) return;
		for (const attr of ['title', 'aria-label', 'placeholder']) {
			const value = element.getAttribute(attr);
			if (!value) continue;
			const direct = map.get(value.trim());
			if (direct) element.setAttribute(attr, direct);
			else {
				let next = value;
				for (const [fr, en] of map) {
					if (fr.length >= 4 && next.includes(fr)) next = next.split(fr).join(en);
				}
				if (next !== value) element.setAttribute(attr, next);
			}
		}
	}

	function translateTree(root = document) {
		if (typeof currentLocale === 'function' && currentLocale() !== 'en') return;
		const map = englishLookup();
		if (root instanceof Element) translateElement(root, map);
		const walker = document.createTreeWalker(root, NodeFilter.SHOW_ELEMENT | NodeFilter.SHOW_TEXT);
		let node;
		while ((node = walker.nextNode())) {
			if (node.nodeType === Node.TEXT_NODE) translateTextNode(node, map);
			else translateElement(node, map);
		}
	}

	function startEnglishLocalizationGuard() {
		translateTree(document.body || document.documentElement);
		const observer = new MutationObserver((mutations) => {
			if (typeof currentLocale === 'function' && currentLocale() !== 'en') return;
			for (const mutation of mutations) {
				if (mutation.type === 'characterData') translateTree(mutation.target.parentElement || document.body);
				else if (mutation.type === 'attributes') translateTree(mutation.target);
				else for (const node of mutation.addedNodes) {
					if (node.nodeType === Node.TEXT_NODE) translateTextNode(node, englishLookup());
					else if (node.nodeType === Node.ELEMENT_NODE) translateTree(node);
				}
			}
		});
		observer.observe(document.documentElement, { subtree: true, childList: true, characterData: true, attributes: true, attributeFilter: ['title', 'aria-label', 'placeholder'] });
		document.getElementById('setting-language')?.addEventListener('change', () => setTimeout(() => translateTree(document.body), 0));
	}

	if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', startEnglishLocalizationGuard, { once: true });
	else startEnglishLocalizationGuard();
})();
'''


def replace_many(text: str, replacements: dict[str, str]) -> tuple[str, int]:
    changed = 0
    for source in sorted(replacements, key=len, reverse=True):
        target = replacements[source]
        count = text.count(source)
        if count:
            text = text.replace(source, target)
            changed += count
    return text, changed


def patch_text_file(path: Path, replacements: dict[str, str]) -> int:
    original = path.read_text(encoding="utf-8")
    patched, count = replace_many(original, replacements)
    if patched != original:
        path.write_text(patched, encoding="utf-8", newline="\n")
    return count


def main() -> None:
    html_count = patch_text_file(INDEX, HTML_REPLACEMENTS)
    rust_count = patch_text_file(MAIN, RUST_REPLACEMENTS)

    app_text = APP.read_text(encoding="utf-8")
    injected = False
    if JS_MARKER not in app_text:
        APP.write_text(app_text.rstrip() + JS_HELPER + "\n", encoding="utf-8", newline="\n")
        injected = True

    print(f"English localization: {html_count} static HTML replacements, {rust_count} native-menu replacements, runtime guard {'added' if injected else 'already present'}.")


if __name__ == "__main__":
    main()
