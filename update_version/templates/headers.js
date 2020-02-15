$.ajax({
    type: 'POST',
    beforeSend: function(request) {
      request.setRequestHeader("Authority", JSON.stringify(select.value));
    },

    url: "/delete_profile",
    contentType: 'application/json;charset=UTF-8',
    data: "json: " + JSON.stringify(select.value),
});