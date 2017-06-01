package controllers


import play.api.mvc.{
  Action => PlayAction,
  Call => PlayCall,
  Controller => PlayController,
  Result => PlayResult,
  Results => PlayResults
}


class Application extends PlayController {

  def index = PlayAction {
    PlayResults.Ok(views.html.index("Your new application is ready."))
  }

}
