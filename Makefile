.PHONY: sdist pin-spec-version rpms debs check-json-spec-docs sync-json-spec-docs

sdist:
	python3 -m build --sdist

# libcobblersignatures.spec hardcodes Version, which rpmbuild uses to compute
# Source0's expected filename before dist/ exists. Sync it to the version the
# sdist we just built actually has.
pin-spec-version: sdist
	@sed -ri 's/^(Version:[[:space:]]*).*/\1'"$$(basename dist/*.tar.gz .tar.gz | sed 's/^libcobblersignatures-//')"'/' libcobblersignatures.spec

rpms: pin-spec-version
	mkdir -p rpm-build
	cp dist/*.gz rpm-build/
	rpmbuild --define "_topdir %(pwd)/rpm-build" \
	--define "_builddir %{_topdir}" \
	--define "_rpmdir %{_topdir}" \
	--define "_srcrpmdir %{_topdir}" \
	--define "_specdir %{_topdir}" \
	--define '_rpmfilename %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm' \
	--define "_sourcedir  %{_topdir}" \
	-ba libcobblersignatures.spec

debs: ## Creates a native Debian package into deb-build/.
	@VERSION="$${SETUPTOOLS_SCM_PRETEND_VERSION:-$$(python3 -m setuptools_scm)}"; \
	DEBFULLNAME="The Cobbler Authors" DEBEMAIL="cobbler.project@gmail.com" \
	dch --newversion "$$VERSION" --distribution unstable --nomultimaint "Automated build."
	@debuild -us -uc
	@mkdir -p deb-build
	@cp ../libcobblersignatures_* deb-build/

check-json-spec-docs: ## Verifies the JSON-spec schema and docs table match the Osversion docstrings.
	python3 -m scripts.sync_json_spec_docs --check

sync-json-spec-docs: ## Regenerates the JSON-spec schema descriptions and docs table from the Osversion docstrings.
	python3 -m scripts.sync_json_spec_docs
