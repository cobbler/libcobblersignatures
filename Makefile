.PHONY: sdist pin-spec-version rpms

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
