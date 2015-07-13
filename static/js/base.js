$(function(){
	$('#general-attachment').click(function(){
		$('#attachment-file')[0].value = '';
		$('#attachment-name')[0].innerHTML = '';
		$('#attachment-file')[0].accept = 'file/*';
		$('#attachment-file').click();
	});
	
	$('#image-attachment').click(function(){
		$('#attachment-file')[0].value = '';
		$('#attachment-name')[0].innerHTML = '';
		$('#attachment-file')[0].accept = "image/*";
		$('#attachment-file').click();
	});
	
	$('#video-attachment').click(function(){
		$('#attachment-file')[0].value = '';
		$('#attachment-name')[0].innerHTML = '';
		$('#attachment-file')[0].accept = "video/*";
		$('#attachment-file').click();
	});
	
	$('#audio-attachment').click(function(){
		$('#attachment-file')[0].value = '';
		$('#attachment-name')[0].innerHTML = '';
		$('#attachment-file')[0].accept = "audio/*";
		$('#attachment-file').click();
	});
	
	$('#attachment-file').change(function(){
		$('#attachment-name')[0].innerHTML = $('#attachment-file').val();
	});
	
    $('.post-form').submit(function(e){
        $('#submit-post').button('loading');
        add_post(e.currentTarget);
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
    
    $('.share-post').click(function(e){
    	id = e.currentTarget.dataset.id;
    	url = e.currentTarget.href;
    	share_post(id,url);
    	return false;
    });
    
    $('#floating-close-area').click(function(){
    	hide_floating_notice();
    });
    
    $('.edit-comment-form').submit(function(e){
        $('#submit-update-comment').button('loading');
        update_comment(e.currentTarget);
        return false;
    });
});

var csrf = $('meta[name=csrfmiddlewaretoken]').attr("content");

function show_floating_notice(data)
{
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
}

function hide_floating_notice()
{
	$('#floating-notice')[0].innerHTML = '';
	$('.floating-notice-wrapper').css("display","none");
	$("body").css('height','auto');
	$("body").css('overflow','auto');
}

function add_post(form){
	var data = new FormData(form);
	
	success = function(data, textStatus, XMLHttpRequest) {
				show_floating_notice(data);
				$('#post-upload-status').hide();
				form.reset();
				$('#submit-post').button('reset');
		};
	error = function(data, error){
		alert('error occurred! post could not be posted');
		$('#post-upload-status').hide();
		$('#submit-post').button('reset');
	};
	
	beforeSendHandler = function(){
		$('#attachment-name')[0].innerHTML = '';
		$('#post-upload-status').show();
	};
	
	$.ajax({
        url: form.action,
        type: 'POST',        
        async : true,
        success: success,
        error: error,
        data : data,
        contentType: false,
        processData: false,
        beforeSend: beforeSendHandler,
        xhr: function() { 
            var myXhr = $.ajaxSettings.xhr();
            if(myXhr.upload){ 
                myXhr.upload.addEventListener('progress',progressHandlingFunction, false);
            }
            return myXhr;
        },
    });
	return false;
}

function progressHandlingFunction(e){
    if(e.lengthComputable){
        $('progress').attr({value:e.loaded,max:e.total});
    }
}

function add_comment(post_id){
	var form = $('#comment-form-'+post_id)[0];
	var data = {};
	for (var i = 0; i < form.length; i++) {
		data[form[i].name] = form[i].value;
	}
	
	success = function(data, textStatus, XMLHttpRequest) {
				show_floating_notice(data);
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

function edit_comment(e)
{
	var id = e.dataset.comment_id;
	form = $('#dummy-edit-comment-form')[0];
	form.action = e.href;
	form[1].value = id;
	show_floating_notice($('#dummy-comment-form-wrapper')[0].innerHTML);
	$("#dummy-edit-comment-form")[0].id = "edit-comment-form-"+id;
	$("#edit-comment-form-"+id)[0][2].value = $('#comment-content-'+id)[0].innerHTML;
	$("#edit-comment-form-"+id)[0].dataset.comment_id = id;
	return false;
}

function update_comment(form)
{
	var id = form.dataset.comment_id;
	var data = {};
	for (var i = 0; i < form.length; i++) {
		data[form[i].name] = form[i].value;
	}
	
	var comment = data['comment'];
	
	success = function(data, textStatus, XMLHttpRequest){
		$('#comment-content-'+id)[0].innerHTML = comment;
		hide_floating_notice();		
	};
	
	error = function(data){
		alert('error occurred! comment could not be edited');
	};
	
	$.ajax({
			url : form.action,
			type : 'POST',
			async : true,
			data : data,
			success : success,
			error : error
		});
}

function share_post(id,url)
{
	success = function(data, textStatus, XMLHttpRequest){
		show_floating_notice(data);		
	};
	
	error = function(data){
		alert('error occurred! your network connection is not working or post has been deleted.');
		console.log(data);
	};
	
	$.ajax({
			url : url,
			type : 'GET',
			async : true,
			success : success,
			error : error
		});
	return false;
}





