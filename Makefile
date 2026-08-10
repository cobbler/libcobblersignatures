.PHONY: sdist pin-spec-version rpms debs check-json-spec-docs sync-json-spec-docs lint-docs

sdist:
	rm -rf dist
	python3 -m build --sdist

# libcobblersignatures.spec and libcobblersignatures.dsc hardcode Version,
# which rpmbuild/dpkg-source use to compute Source0/DEBTRANSFORM-TAR's
# expected filename before dist/ exists. Sync them to the version the
# sdist we just built actually has.
pin-spec-version: sdist
	@VERSION="$$(basename dist/*.tar.gz .tar.gz | sed -E 's/^libcobblersignatures-([0-9]+\.[0-9]+\.[0-9]+).*/\1/')"; \
	sed -ri 's/^(Version:[[:space:]]*).*/\1'"$$VERSION"'/' libcobblersignatures.spec; \
	sed -ri 's/^(Version:[[:space:]]*).*/\1'"$$VERSION"'/' libcobblersignatures.dsc; \
	sed -ri 's/^(DEBTRANSFORM-TAR:[[:space:]]*).*/\1libcobblersignatures-'"$$VERSION"'.tar.gz/' libcobblersignatures.dsc

rpms: sdist ## Creates a native RPM package into rpm-build/.
	@mkdir -p rpm-build
	@FULL_VERSION="$$(basename dist/*.tar.gz .tar.gz | sed 's/^libcobblersignatures-//')"; \
	sed -r 's/^(Version:[[:space:]]*).*/\1'"$$FULL_VERSION"'/' libcobblersignatures.spec > rpm-build/libcobblersignatures.spec
	cp dist/*.gz rpm-build/
	rpmbuild --define "_topdir %(pwd)/rpm-build" \
	--define "_builddir %{_topdir}" \
	--define "_rpmdir %{_topdir}" \
	--define "_srcrpmdir %{_topdir}" \
	--define "_specdir %{_topdir}" \
	--define '_rpmfilename %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm' \
	--define "_sourcedir  %{_topdir}" \
	-ba rpm-build/libcobblersignatures.spec

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

lint-docs: ## Runs the same rstcheck/doc8 linters as the "docs" CI job against docs/.
	rstcheck -r docs
	doc8 --ignore D001 docs
