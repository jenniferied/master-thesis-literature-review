# Makefile for Master Thesis Literature Review

.PHONY: help explainer lit-review all lint lint-fix clean analysis

help:
	@echo "Master Thesis Literature Review - Build Commands"
	@echo ""
	@echo "PDF Generation:"
	@echo "  explainer         Build AI/ML Foundations Explainer PDF"
	@echo "  lit-review        Build Literature Review Chapter PDF"
	@echo "  all               Build all PDFs"
	@echo ""
	@echo "Analysis:"
	@echo "  analysis          Run bibliometric analysis"
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

# Build all PDFs
all: explainer lit-review

# Build explainer PDF using thesis template
explainer:
	@echo "Building AI/ML Foundations Explainer PDF..."
	@cd drafts && pandoc ai_ml_foundations_explainer.md \
		--template=../templates/thesis.tex \
		--pdf-engine=lualatex \
		--toc \
		-V title="Master Thesis Appendix B: AI/ML Foundations Explainer" \
		-V author="Jennifer Meier" \
		-V date="December 2025" \
		-V institute="Technische Hochschule Ostwestfalen-Lippe" \
		-V department="Department of Media Production" \
		-V course="Master Media Production" \
		-o ../export/ai_ml_foundations_explainer.pdf 2>&1 || \
		(echo "Thesis template failed, using simple build..."; \
		 pandoc ai_ml_foundations_explainer.md \
			--pdf-engine=lualatex \
			--toc \
			-V geometry:margin=2.54cm \
			-o ../export/ai_ml_foundations_explainer.pdf)
	@echo "✓ Explainer PDF: export/ai_ml_foundations_explainer.pdf"

# Build literature review PDF using thesis template
lit-review:
	@echo "Building Literature Review Chapter PDF..."
	@cd drafts && pandoc literature_review_chapter.md \
		--template=../templates/thesis.tex \
		--pdf-engine=lualatex \
		--toc \
		-V title="Master Thesis Appendix A: Scoping Literature Review" \
		-V author="Jennifer Meier" \
		-V date="December 2025" \
		-V institute="Technische Hochschule Ostwestfalen-Lippe" \
		-V department="Department of Media Production" \
		-V course="Master Media Production" \
		-o ../export/literature_review_chapter.pdf 2>&1 || \
		(echo "Thesis template failed, using simple build..."; \
		 pandoc literature_review_chapter.md \
			--pdf-engine=lualatex \
			--toc \
			-V geometry:margin=2.54cm \
			-o ../export/literature_review_chapter.pdf)
	@echo "✓ Literature Review PDF: export/literature_review_chapter.pdf"

# Run bibliometric analysis
analysis:
	@echo "Running bibliometric analysis..."
	@python3 scripts/bibliometric_analysis.py
	@echo "✓ Analysis complete: outputs/bibliometric_summary.md"

# Lint all markdown files
lint:
	@echo "Running markdownlint..."
	@npx markdownlint-cli "drafts/**/*.md" "*.md" || true
	@echo "✓ Lint complete"

# Auto-fix lint issues
lint-fix:
	@echo "Auto-fixing lint issues..."
	@npx markdownlint-cli --fix "drafts/**/*.md" "*.md" || true
	@echo "✓ Lint fixes applied"

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	@rm -f export/*.pdf export/*.md
	@rm -f drafts/*.aux drafts/*.log drafts/*.out drafts/*.toc
	@echo "✓ Cleaned generated files"
