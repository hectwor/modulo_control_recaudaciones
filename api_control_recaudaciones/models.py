from __future__ import unicode_literals

from django.db import models

class Accede(models.Model):
    id_tu = models.ForeignKey('TipoUsuario', models.DO_NOTHING, db_column='id_tu', primary_key=True)
    id_mod = models.ForeignKey('Modulo', models.DO_NOTHING, db_column='id_mod')

    class Meta:
        managed = False
        db_table = 'accede'
        unique_together = (('id_tu', 'id_mod'),)


class Administrativo(models.Model):
    id_admin = models.SmallIntegerField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    codigo = models.CharField(unique=True, max_length=8)
    dni = models.CharField(unique=True, max_length=8)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'administrativo'


class Alumno(models.Model):
    id_alum = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_facultad = models.ForeignKey('Facultad', models.DO_NOTHING, db_column='id_facultad')
    ape_nom = models.CharField(unique=True, max_length=70)
    codigo = models.CharField(unique=True, max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alumno'


class ApiControlRecaudacionesAlumno(models.Model):
    id_alum = models.CharField(primary_key=True, max_length=10)
    id_usuario = models.IntegerField()
    id_facultad = models.IntegerField()
    ape_nom = models.CharField(max_length=70)
    codigo = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'api_control_recaudaciones_alumno'


class ApiControlRecaudacionesConcepto(models.Model):
    id_concepto = models.CharField(primary_key=True, max_length=10)
    concepto = models.CharField(max_length=6)
    concepto_a = models.CharField(max_length=6)
    concepto_b = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'api_control_recaudaciones_concepto'


class ApiControlRecaudacionesRecaudacion(models.Model):
    id_rec = models.CharField(primary_key=True, max_length=10)
    id_alu = models.IntegerField()
    id_concepto = models.IntegerField()
    moneda = models.CharField(max_length=3)
    numero_voucher = models.CharField(max_length=10)
    importe = models.IntegerField()
    carnet = models.CharField(max_length=30)
    autoseguro = models.CharField(max_length=30)
    ave = models.CharField(max_length=30)
    devol_tran = models.CharField(max_length=30)
    observacion = models.CharField(max_length=100)
    fecha = models.DateField()
    flag_pago = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'api_control_recaudaciones_recaudacion'


class Auditoria(models.Model):
    id_admin = models.ForeignKey(Administrativo, models.DO_NOTHING, db_column='id_admin', primary_key=True)
    id_rec = models.ForeignKey('Recaudaciones', models.DO_NOTHING, db_column='id_rec')
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'auditoria'
        unique_together = (('id_admin', 'id_rec'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Concepto(models.Model):
    id_concepto = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    concepto = models.CharField(unique=True, max_length=6)
    concep_a = models.CharField(max_length=3)
    concep_b = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'concepto'


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nom_curso = models.CharField(max_length=40)
    id_programa = models.ForeignKey('Programa', models.DO_NOTHING, db_column='id_programa')

    class Meta:
        managed = False
        db_table = 'curso'


class DatosAcademicos(models.Model):
    id_dat_academicos = models.AutoField(primary_key=True)
    id_docente = models.ForeignKey('Docente', models.DO_NOTHING, db_column='id_docente')
    id_tip_grado = models.ForeignKey('TipoGrado', models.DO_NOTHING, db_column='id_tip_grado')
    mencion_grado = models.CharField(max_length=60)
    centro_estudios = models.CharField(max_length=60)
    pais_estudios = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'datos_academicos'


class Dia(models.Model):
    id_dia = models.CharField(primary_key=True, max_length=1)
    nom_dia = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'dia'


class Directiva(models.Model):
    id_direc = models.SmallIntegerField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    codigo = models.CharField(unique=True, max_length=8)
    dni = models.CharField(unique=True, max_length=8)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'directiva'


class Disponibilidad(models.Model):
    id_disponibilidad = models.AutoField(primary_key=True)
    id_docente = models.ForeignKey('Docente', models.DO_NOTHING, db_column='id_docente')
    id_dia = models.ForeignKey(Dia, models.DO_NOTHING, db_column='id_dia')
    hr_inicio = models.CharField(max_length=2)
    hr_fin = models.CharField(max_length=2)
    tot_hrs = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'disponibilidad'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Docente(models.Model):
    id_docente = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    nom_docente = models.CharField(max_length=50)
    ape_docente = models.CharField(max_length=50)
    codigo_docente = models.CharField(max_length=10)
    dni_docente = models.CharField(max_length=8)
    email_docente = models.CharField(max_length=70)
    celular_docente = models.CharField(max_length=9)
    genero = models.CharField(max_length=1)
    pagina_web = models.CharField(max_length=50)
    foto = models.BinaryField(blank=True, null=True)
    fecha_nac = models.DateField()
    pais = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80)
    sunedu_le = models.CharField(max_length=2)
    categoria = models.CharField(max_length=30)
    regimen_dedicacion = models.CharField(max_length=30)
    cv = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'docente'


class ExperienciaAsesorDocente(models.Model):
    id_exp_asesor_docente = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    id_docente = models.ForeignKey(Docente, models.DO_NOTHING, db_column='id_docente')
    universidad = models.CharField(max_length=80)
    tesis = models.CharField(max_length=70)
    tesista = models.CharField(max_length=70)
    repositorio = models.CharField(max_length=70)
    fecha_aceptacion = models.DateField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiencia_asesor_docente'


class ExperienciaLaboral(models.Model):
    id_exp_laboral = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    id_docente = models.ForeignKey(Docente, models.DO_NOTHING, db_column='id_docente')
    empresa = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'experiencia_laboral'


class Facultad(models.Model):
    id_facultad = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    nombre = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'facultad'


class LaboralDocente(models.Model):
    id_laboral_doc = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    id_docente = models.ForeignKey(Docente, models.DO_NOTHING, db_column='id_docente')
    universidad = models.CharField(max_length=80)
    tipo_docente = models.CharField(max_length=50)
    fecha_inicio = models.DateField(blank=True, null=True)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laboral_docente'


class Modulo(models.Model):
    id_mod = models.SmallIntegerField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'modulo'


class NivelesPrograma(models.Model):
    id_niveles_program = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    id_docente = models.ForeignKey(Docente, models.DO_NOTHING, db_column='id_docente')
    pregrado = models.CharField(max_length=2)
    maestria = models.CharField(max_length=2)
    doctorado = models.CharField(max_length=2)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'niveles_programa'


class Preferencia(models.Model):
    id_preferencia = models.AutoField(primary_key=True)
    id_docente = models.ForeignKey(Docente, models.DO_NOTHING, db_column='id_docente')
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso')

    class Meta:
        managed = False
        db_table = 'preferencia'


class Programa(models.Model):
    id_programa = models.SmallIntegerField(primary_key=True)
    nom_programa = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'programa'


class ProyectoInvestigacion(models.Model):
    id_proyecto_invest = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    id_docente = models.ForeignKey(Docente, models.DO_NOTHING, db_column='id_docente')
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    area_ocde = models.CharField(max_length=50)
    createdat = models.DateTimeField(blank=True, null=True)
    updatedat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proyecto_investigacion'


class Recaudaciones(models.Model):
    id_rec = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    id_alum = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='id_alum')
    id_concepto = models.ForeignKey(Concepto, models.DO_NOTHING, db_column='id_concepto')
    moneda = models.CharField(max_length=3, blank=True, null=True)
    numero_voucher = models.CharField(unique=True, max_length=10, blank=True, null=True)
    importe = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    carnet = models.CharField(max_length=30, blank=True, null=True)
    autoseguro = models.CharField(max_length=30, blank=True, null=True)
    ave = models.CharField(max_length=30, blank=True, null=True)
    devol_tran = models.CharField(max_length=30, blank=True, null=True)
    observacion = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    flag_pago = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'recaudaciones'


class TipoGrado(models.Model):
    id_tip_grado = models.CharField(primary_key=True, max_length=2)
    nom_tip_grado = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_grado'


class TipoUsuario(models.Model):
    id_tu = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    nombre_tipo = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuario(models.Model):
    id_usuario = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    id_tu = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='id_tu')
    user_name = models.CharField(unique=True, max_length=30)
    pass_field = models.CharField(db_column='pass', max_length=30)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'usuario'
