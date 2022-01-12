from datetime import datetime

from flask import Blueprint, render_template, request, url_for, g
from werkzeug.utils import redirect

from .. import db
from ..models import Diary
from ..forms import DiaryForm, MusicRecForm
from pybo.views.auth_views import login_required

import pandas as pd
import numpy as np
from numpy import dot
from numpy.linalg import norm
import warnings
warnings.filterwarnings('ignore')




bp = Blueprint('diary', __name__, url_prefix='/diary')


@bp.route('/list/')
def _list():
    diary_list = Diary.query.order_by(Diary.create_date.desc())
    return render_template('diary/diary_list.html', diary_list=diary_list)


@bp.route('/detail/<int:diary_id>/')
def detail(diary_id):
    form = MusicRecForm()
    diary = Diary.query.get(diary_id)
    return render_template('diary/diary_detail.html', diary=diary, form=form)


@bp.route('/create/', methods=['GET', 'POST'])
@login_required
def create():
    form = DiaryForm()
    if request.method == 'POST' and form.validate_on_submit():
        diary = Diary(subject=form.subject.data, content=form.content.data, create_date=datetime.now(), user=g.user)
        db.session.add(diary)
        db.session.commit()
        return render_template('diary/diary_detail.html', diary=diary, form=form) # 작성을 하면 목록 화면(main.index)으로 가는 상태니까 바로 디테일 화면(diary.detail)으로 가게끔
    return render_template('diary/diary_form.html', form=form)
