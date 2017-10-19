srpm:
	spectool -g $(spec_path)
	rpmbuild -bs -D "dist %{nil}" -D "_srcrpmdir $(outdir)" --nodeps $(spec_path)
