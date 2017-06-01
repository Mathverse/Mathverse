package models


import slick.jdbc.PostgresProfile.api._


case class Solution(id: Long, text: String)


class SolutionTableDef(tag: Tag) extends Table[Solution](tag, "solutions") {
  def id = column[Long]("id", O.PrimaryKey, O.AutoInc)
  def text = column[String]("text")

  def * = (id, text) <>(Solution.tupled, Solution.unapply)
}
