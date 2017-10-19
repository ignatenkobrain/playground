srpm:
	dnf -y --setopt=tsflags=nodocs install rpmdevtools rpm-build
	spectool -g $(spec_path)
	rpmbuild -bs -D "dist %{nil}" -D "_srcrpmdir $(outdir)" --nodeps $(spec_path)
