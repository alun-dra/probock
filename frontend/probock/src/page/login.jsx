import React, { useState } from 'react';
import {
    Avatar,
    Button,
    CssBaseline,
    TextField,
    FormControlLabel,
    Checkbox,
    Link,
    Grid,
    Typography,
    Container,
} from '@material-ui/core';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
    paper: {
        marginTop: theme.spacing(8),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        padding: theme.spacing(3),
        border: '1px solid rgba(0, 0, 0, 0.2)', // Agrega un borde con transparencia
        boxShadow: '0px 2px 4px rgba(0, 0, 0, 0.2)', // Agrega una sombra
        borderRadius: theme.shape.borderRadius,

    },
    avatar: {
        margin: theme.spacing(1),
        backgroundColor: 'black', // Cambia el color de fondo del Avatar a negro
        '& .iconContainer': {
            color: 'white', // Cambia el color del ícono a blanco
        },
    },
    form: {
        width: '100%',
        marginTop: theme.spacing(1),
    },
    submit: {
        margin: theme.spacing(3, 0, 2),
        backgroundColor: 'black', // Cambia el color de fondo del botón a negro
        color: 'white', // Cambia el color del texto del botón a negro
    },
}));

const Login = () => {
    const classes = useStyles();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleEmailChange = (e) => {
        setEmail(e.target.value);
    };

    const handlePasswordChange = (e) => {
        setPassword(e.target.value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(`Email: ${email}, Password: ${password}`);
    };

    return (
        <Container component="main" maxWidth="xs">
            <CssBaseline />
            <div className={classes.paper}>
                <Avatar className={classes.avatar}>
                    <div className="iconContainer">
                        <LockOutlinedIcon />
                    </div>
                </Avatar>
                <Typography component="h1" variant="h5">
                    Iniciar sesión
                </Typography>
                <form className={classes.form} onSubmit={handleSubmit}>
                    <TextField
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        id="email"
                        label="Correo electrónico"
                        name="email"
                        autoComplete="email"
                        autoFocus
                        value={email}
                        onChange={handleEmailChange}
                    />
                    
                    <TextField
                        variant="outlined"
                        margin="normal"
                        required
                        fullWidth
                        name="password"
                        label="Contraseña"
                        type="password"
                        id="password"
                        autoComplete="current-password"
                        value={password}
                        onChange={handlePasswordChange}
                    />
                    <FormControlLabel
                        control={<Checkbox value="remember" color="primary" />}
                        label="Recordarme"
                    />
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        color="primary"
                        className={classes.submit}
                    >
                        Iniciar sesión
                    </Button>
                    <Grid container>
                        <Grid item xs>
                            <Link href="#" variant="body2" style={{ color: 'black' }}>
                                ¿Olvidaste tu contraseña?
                            </Link>
                        </Grid>
                        <Grid item>
                            <Link href="" variant="body2" style={{ color: 'black' }}>
                                ¿No tienes una cuenta? Regístrate
                            </Link>
                        </Grid>
                    </Grid>
                </form>
            </div>
        </Container>
    );
};

export default Login;
