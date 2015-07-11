$(function(){
    $('#status-form').submit(function(){
        $('#submit-status').button('loading');
        add_status();
        return false;
    });
    
    $('#floating-close-area').click(function(){
    	$('.floating-notice-wrapper').css("display","none");
    	$("body").css('height','auto');
		$("body").css('overflow','auto');
    });
});

function add_status(){
	var form = $('#status-form')[0];
	var data = {};
	for (var i = 0; i < form.length; i++) {
		data[form[i].name] = form[i].value;
	}
	
	success = function(data, textStatus, XMLHttpRequest) {
				$("#floating-notice")[0].innerHTML = data;
				$('.floating-notice-wrapper').css("display","block");
				
				var h = 0;
				if($('.floating-notice').height()+200 > $(window).height())
					h = $('.floating-notice').height()+200 ;
				else
					h = $(window).height();
					
				$(".floating-close-area").css('height',h);
				$("body").css('height',h);
				$("body").css('overflow','hidden');
				form.reset();
				$('#submit-status').button('reset');
		};
	error = function(){
		alert('error occurred! post could not be posted');
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
