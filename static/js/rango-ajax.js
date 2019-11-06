(function () {
  'use script';

    function Category()
    {
        this.init();
        this.addLikeListener();
        this.addSuggestionListener();
    }

    Category.prototype =
    {
        init: function()
        {
            this.likeEl = $('#likes');
            this.id = this.likeEl.attr('data-catid');
            this.likeEndpoint = '/rango/like_category';
            this.suggestionEl = $('#suggestion');
            this.suggectionEndpoint = '/rango/suggest_category';
        },

        addLikeListener: function()
        {
            if (this.likeEl) {
                var self = this;
                this.likeEl.click(function(){
                    $.get(self.likeEndpoint, {category_id: self.id}, function(data){
                        $('#like_count').html(data);
                    });
                });
            }
        },

        addSuggestionListener: function()
        {
            if (this.suggestionEl) {
                var self = this;
                this.suggestionEl.keyup(function(){
                    if (self.suggestionEl.val() == '') {
                        $('#suggested_categories').html('');
                    } else {
                        $.get(self.suggectionEndpoint, {suggestion: self.suggestionEl.val()}, function(data){
                            $('#suggested_categories').html(data);
                        });
                    }
                });
            }
        }
    }

    $(document).ready(function() {
        new Category();
    });


//  document.addEventListener('DOMContentLoaded', function () {
//
//  });
})()