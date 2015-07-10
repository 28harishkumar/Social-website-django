$(function(){
    $('#status-form').submit(function(){
        $('#submit-status').button('loading');
        add_status();
        return false;
    });
});

function add_status(){
	var form = $('#status-form')[0];
	var data = {};
	for (var i = 0; i < form.length; i++) {
		data[form[i].name] = form[i].value;
	}
	
	success = function(data, textStatus, XMLHttpRequest) {
				alert(data);
				form.reset();
				$('#submit-status').button('reset');
		};
	error = function(){
		alert('error');
		$('#submit-status').button('reset');
	};
	
	$.ajax({
			url : form.action,
			type : form.method.toUpperCase(),
			dataType : 'text',
			async : true,
			data : data,
			success : success,
			error : error
		});
	return false;
}
