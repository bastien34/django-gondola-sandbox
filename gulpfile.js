var gulp = require('gulp');
var less = require('gulp-less');
var path = require('path');

gulp.task('less', function () {
  return gulp.src('static/gondola/less/*.less')
    .pipe(less({
      paths: [ path.join(__dirname, 'less', 'includes') ]
    }))
    .on('error', onError)
    .pipe(gulp.dest('static/gondola/css'));
});

gulp.task('default', function () {
   gulp.watch('static/gondola/less/**/*.less', ['less']);
});

function onError(err){
    console.log(err);
    this.emit('end');
}