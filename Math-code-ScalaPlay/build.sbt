lazy val `Math-ScalaPlay-project` =
  (project in file("."))
    .enablePlugins(PlayScala)
    .settings(
      name := "Math",

      organization := "Nguyen Minh Ha",

      version := "0.0.0",

      scalaVersion := "2.11.11",

      libraryDependencies ++= Seq(
        jdbc,
        cache,
        ws,
        specs2 % Test
      ),

      unmanagedResourceDirectories in Test <+=  baseDirectory ( _ /"target/web/public/test" ),

      resolvers += "scalaz-bintray" at "https://dl.bintray.com/scalaz/releases"
    )
