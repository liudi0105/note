#### maven install file

```bash
mvn install:install-file -DgroupId=javax.transaction -DartifactId=jta -Dpackaging=jar -Dversion=1.0.1B -Dfile=ojdbc14-10.2.0.1.0.jar -DgeneratePom=true
-DarchetypeCatalog=internal


mvn install:install-file -DgroupId=com.lowagie -DartifactId=itext -Dpackaging=jar -Dversion=10.2.0.1.0 -Dfile=itext-2.1.7.js5.jar -DgeneratePom=true
```

