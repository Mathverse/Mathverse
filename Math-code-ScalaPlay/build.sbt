lazy val `Math-ScalaPlay-project` =
  (project in file("."))
    .enablePlugins(PlayScala)
    .settings(
      name := "Math",

      organization := "Nguyen Minh Ha",

      version := "0.0.0",

      scalaVersion := "2.11.11",

      resolvers ++= Seq(
        "scalaz-bintray" at "https://dl.bintray.com/scalaz/releases"
      ),

      libraryDependencies ++= Seq(
        jdbc,
        cache,
        ws,
        specs2 % Test,

        "org.postgresql" % "postgresql" % "9.4.1212"
      ),

      unmanagedResourceDirectories in Test <+= baseDirectory ( _ /"target/web/public/test" )
    )
