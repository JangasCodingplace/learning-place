$("[data-target='#searchResultModal']").click(function(){
  $("#searchResultModalLabel").text("Loading ...")
  $("#searchResultModalBody").text("Loading ...")

  $.ajax({
    url: '{% url "course_wiki_detail" "REPLACE_ID" %}'.replace("REPLACE_ID", $(this).attr("data-entity-id")),
    success: function (data){
      $("#searchResultModalLabel").text(data.title)
      $("#searchResultModalBody").text(data.body)
      MathJax.typeset();
    }
  })
})
