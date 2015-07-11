$(function(){
    $('#post-form').submit(function(){
        $('#submit-post').button('loading');
        add_post();
        return false;
    });
    
    $('#comment-input').keypress(function(e){
    	if(e.which == 13)
    	{
    		add_comment();
        	return false;
    	}
    });
    
    $('.show-comment').click(function(e){
    	id = e.currentTarget.dataset.id;
    	fetch_comments(id);
    	return false;
    });
    
    $('#floating-close-area').click(function(){
    	$('.floating-notice-wrapper').css("display","none");
    	$("body").css('height','auto');
		$("body").css('overflow','auto');
    });
});

function add_post(){
	var form = $('#post-form')[0];
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
				$('#submit-post').button('reset');
		};
	error = function(){
		alert('error occurred! post could not be posted');
		$('#submit-post').button('reset');
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

function add_comment(){
	var form = $('#comment-form')[0];
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
		};
	error = function(){
		alert('error occurred! comment could not be posted');
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

function fetch_comments(id)
{
	success = function(data, textStatus, XMLHttpRequest) {
				$("#comment-on-"+id)[0].innerHTML = data;
		};
	
	error = function(){
		alert('error occurred! comment could not be posted');
	};
	
	$.ajax({
			url : '/post/'+id+'/comments',
			type : 'GET',
			async : false,
			success : success,
			error : error
		});
}





