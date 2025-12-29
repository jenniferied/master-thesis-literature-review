# Makefile for Master Thesis Literature Review

.PHONY: help explainer explainer-pdf lint lint-fix clean

help:
	@echo "Master Thesis Literature Review - Build Commands"
	@echo ""
	@echo "PDF Generation:"
	@echo "  explainer         Build AI/ML Foundations Explainer PDF"
	@echo "  explainer-copy    Copy explainer markdown to export/"
	@echo ""
	@echo "Quality Checks:"
	@echo "  lint              Run markdownlint on all markdown files"
	@echo "  lint-fix          Auto-fix lint issues where possible"
	@echo ""
	@echo "Other:"
	@echo "  clean             Remove generated files"
	@echo ""
	@echo "Requirements:"
	@echo "  - LuaLaTeX (via TeX Live or MacTeX)"
	@echo "  - Pandoc (https://pandoc.org/)"
	@echo "  - markdownlint-cli (npm install -g markdownlint-cli)"

# Build explainer PDF
explainer:
	@echo "Building AI/ML Foundations Explainer PDF..."
	@python3 scripts/build-explainer.py
	@echo "✓ Explainer PDF: export/ai_ml_foundations_explainer.pdf"

# Alias for explainer
explainer-pdf: explainer

# Copy explainer to export (markdown only)
explainer-copy:
	@echo "Copying explainer to export..."
	@python3 scripts/build-explainer.py --merge-only
	@echo "✓ Copied to export/ai_ml_foundations_explainer.md"

# Lint all markdown files
lint:
	@echo "Running markdownlint..."
	@markdownlint "drafts/**/*.md" "*.md" || true
	@echo "✓ Lint complete"

# Auto-fix lint issues
lint-fix:
	@echo "Auto-fixing lint issues..."
	@markdownlint --fix "drafts/**/*.md" "*.md" || true
	@echo "✓ Lint fixes applied"

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	@rm -f export/*.pdf export/*.md
	@rm -f drafts/*.aux drafts/*.log drafts/*.out drafts/*.toc
	@echo "✓ Cleaned generated files"
