from flask_assets import Bundle, Environment, Filter


class ConcatFilter(Filter):
    """
    Filter that merges files, placing a semicolon between them.
    """
    def concat(self, out, hunks, **kw):
        out.write(';'.join([h.data() for h, info in hunks]))


css_login = Bundle(
    'assets/css/all.css',
    'assets/css/blue.css',
    'assets/css/adminlte.css',
    filters=('rcssmin', 'cssrewrite'),
    output='generated/login.css')

js_login = Bundle(
    'assets/js/jquery.js',
    'assets/js/bootstrap.js',
    'assets/js/icheck.js',
    'assets/js/knockout-latest.js',
    'custom/js/custom.js',
    filters=(ConcatFilter, 'rjsmin'),
    output='generated/login.js')

js_validation = Bundle(
    'assets/js/validator.js',
    output='generated/validation.js')

css_main = Bundle(
    'assets/css/all.css',
    'assets/css/dataTables.bootstrap4.css',
    'assets/css/blue.css',
    'assets/css/multi-select.css',
    'assets/css/adminlte.css',
    'custom/css/custom.css',
    'assets/css/bootstrap-datepicker.css',
    filters=('rcssmin', 'cssrewrite'),
    output='generated/main.css')

js_main = Bundle(
    'assets/js/jquery.js',
    'assets/js/jquery-ui.js',
    'assets/js/bootstrap.bundle.js',
    'assets/js/jquery.dataTables.js',
    'assets/js/dataTables.bootstrap4.js',
    'assets/js/jquery.sparkline.js',
    'assets/js/jquery.slimscroll.js',
    'assets/js/jquery.validate.js',
    'assets/js/icheck.js',
    'assets/js/fastclick.js',
    'assets/js/moment.js',
    'assets/js/adminlte.js',
    'assets/js/jquery.multi-select.js',
    'assets/js/natural.js',
    'assets/js/jTimeout.js',
    'assets/js/jquery.quicksearch.js',
    'assets/js/knockout-latest.js',
    'custom/js/app-authentication-settings-editor.js',
    'custom/js/custom.js',
    'assets/js/bootstrap-datepicker.js',
    filters=(ConcatFilter, 'rjsmin'),
    output='generated/main.js')

assets = Environment()
assets.register('js_login', js_login)
assets.register('js_validation', js_validation)
assets.register('css_login', css_login)
assets.register('js_main', js_main)
assets.register('css_main', css_main)
