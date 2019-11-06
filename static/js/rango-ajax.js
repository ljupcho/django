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
            this.likeEndpoint = '/rango/like_category';
            this.suggestionEl = $('#suggestion');
            this.suggectionEndpoint = '/rango/suggest_category';
            this.addPageEl = $('#add_page');
            this.addPageEndpoint = '/rango/add_auto_page';
        },

        addLikeListener: function()
        {
            if (this.likeEl) {
                var self = this;
                this.likeEl.click(function(){
                    let input = {
                        category_id: self.likeEl.attr('data-catid')
                    };
                    $.get(self.likeEndpoint, input, function(data){
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
                        let input = {
                            suggestion: self.suggestionEl.val()
                        };
                        $.get(self.suggectionEndpoint, input, function(data){
                            $('#suggested_categories').html(data);
                        });
                    }
                });
            }
        },

        addNewPage: function()
        {
            if (this.addPageEl) {
                var self = this;
                this.addPageEl.click(function(){
                    let input = {
                        category_id: self.addPageEl.attr('data-catid'),
                        title: self.addPageEl.attr('data-title'),
                        url: self.addPageEl.attr('data-url')
                    };
                    $.post(self.addPageEndpoint, input, function(data){
                        $('#pages').html(data);
                    });
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