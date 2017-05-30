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
        // jdbc,   // using Slick for accessing your databases
        cache,
        ws,
        specs2 % Test,
        // evolutions,   // no need to add Play evolutions -- transitive dependency of play-slick-evolutions

        // PostgreSQL
        "org.postgresql" % "postgresql" % "9.4.1212",

        // Slick
        "com.typesafe.play" %% "play-slick" % "2.1.0",
        "com.typesafe.play" %% "play-slick-evolutions" % "2.1.0"
      ),

      unmanagedResourceDirectories in Test <+= baseDirectory ( _ /"target/web/public/test" )
    )
