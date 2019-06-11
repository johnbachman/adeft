import os
import logging

from flask import Flask, session, render_template

# Suppress flask server logging
werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.setLevel(logging.ERROR)
os.environ['WERKZEUG_RUN_MAIN'] = 'true'


def create_app(longforms, scores,
               grounding_map, names_map, pos_labels, outpath):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY='dev',
                            LONGFORMS=longforms,
                            SCORES=scores,
                            OUTPATH=outpath)

    from adeft.gui.ground import ground

    @app.route('/')
    def initialize():
        groundings = [grounding_map[longform] for longform in longforms]
        names = [names_map[grounding] if grounding is not None else None
                 for grounding in groundings]
        labels = _get_labels(groundings)
        groundings = [grounding if grounding is not None else ''
                      for grounding in groundings]
        names = [name if name is not None else '' for name in names]

        session['groundings'] = groundings
        session['names'] = names
        session['labels'] = labels
        session['pos_labels'] = pos_labels

        data = list(zip(longforms, scores, names, groundings, labels))
        return render_template('input.jinja2', data=data,
                               pos_labels=pos_labels)

    app.register_blueprint(ground.bp)
    return app


def _get_labels(groundings):
    labels = sorted(set(grounding for grounding in groundings if grounding))
    labels.extend(['']*(len(groundings) - len(labels)))
    return labels
