KindEditor.ready(function(K) {
    K.create('textarea[name=article]',
        {
            'width':'1000px',
            'height':'400px',
            'uploadJson':'/admin/upload/kindeditor',
        });
});
