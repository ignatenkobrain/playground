srpm:
	dnf -y --setopt=tsflags=nodocs install rpmdevtools rpm-build
	spectool -g $(spec)
	rpmbuild -bs -D "dist %{nil}" -D "_sourcedir $(shell pwd)" -D "_srcrpmdir $(outdir)" --nodeps $(spec)
