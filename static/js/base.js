$(function(){
    $('#post-form').submit(function(){
        $('#submit-post').button('loading');
        add_post();
        return false;
    });
    
    $('.comment-input').keypress(function(e){
    	if(e.which == 13)
    	{
    		if(e.currentTarget.value.trim() !== '')
    			add_comment(e.currentTarget.dataset.post_id);
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

function add_comment(post_id){
	var form = $('#comment-form-'+post_id)[0];
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
			async : true,
			success : success,
			error : error
		});
}

function delete_comment(e)
{
	success = function(data, textStatus, XMLHttpRequest){
		$("#comment-"+e.dataset.comment_id)[0].innerHTML = '';
		$("#comment-"+e.dataset.comment_id).hide();
	};
	
	error = function(){
		alert('error occurred! comment could not be deleted');
	};
	
	$.ajax({
			url : e.href,
			type : 'POST',
			async : true,
			data : { 'csrfmiddlewaretoken' : e.dataset.c},
			success : success,
			error : error
		});
}



