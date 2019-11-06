(function () {
  'use script';

    function Category()
    {
        this.init();
        this.addLikeListener();
    }

    Category.prototype =
    {
        init: function()
        {
            this.likeEl = $('#likes');
            this.id = this.likeEl.attr('data-catid');
            this.endpoint = '/rango/like_category';
        },
        addLikeListener: function()
        {
            var self = this;
            this.likeEl.click(function(){
                self.runAjaxLike();
            });
        },
        runAjaxLike: function()
        {
            $.get(this.endpoint, {category_id: this.id}, function(data){
	            $('#like_count').html(data);
	        });
        }
    }

    $(document).ready(function() {
        new Category();
    });


//  document.addEventListener('DOMContentLoaded', function () {
//
//  });
})()