package models


import slick.jdbc.PostgresProfile.api._


case class Problem(id: Long, text: String)


class ProblemTableDef(tag: Tag) extends Table[Problem](tag, "problems") {
  def id = column[Long]("id", O.PrimaryKey, O.AutoInc)
  def text = column[String]("text")

  def * = (id, text) <>(Problem.tupled, Problem.unapply)
}
