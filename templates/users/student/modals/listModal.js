<script>
    $('#submit').on('click', function(){
		var group = $('#group_select').val();
		var username = $('#username').val();
		var first_name = $('#first-name').val();
		var last_name = $('#last-name').val();
		var birthday = $('.birthday').val();
		var gender = $('#gender').val();
		var email = $('#email').val();
		var password = $('#password').val();
		var phone = $('#phone').val();
		$.ajax({
			type:'POST',
			url: '/api/v1/user/student/create/',
			data: {
				studentgroups:group,
				gender:gender,
				username:username,
				first_name:first_name,
				last_name:last_name,
				birthday:birthday,
				password:password,
				email:email,
				phone:phone,
				csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
			},
			success: function(data){
				window.location = '/users/student-list/{{pk}}';
			}
		})
	});
</script> 