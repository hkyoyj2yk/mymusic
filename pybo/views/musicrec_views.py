from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g
from werkzeug.utils import redirect

from .. import db
from ..forms import MusicRecForm
from ..models import Diary, MusicRec
from .auth_views import login_required

bp = Blueprint('musicrec', __name__, url_prefix='/musicrec')


@bp.route('/recommend/<int:diary_id>', methods=['GET','POST'])
@login_required
def recommend(diary_id):
    form = MusicRecForm()
    diary = Diary.query.get_or_404(diary_id)
    musicname = request.form.get('musicname',False)
    # POST 폼 방식으로 전송된 데이터 항목 중 name 속성이 musicname인 값
    musicrec = MusicRec(musicname=musicname, create_date=datetime.now(), user=g.user)
    diary.musicrec_set.append(musicrec)
    db.session.commit()
    return render_template('diary/diary_detail.html', diary=diary, form=form)