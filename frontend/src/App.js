import { CssBaseline, Button } from "@mui/material";

function start() {
  fetch("/api/start");
}

function stop() {
  fetch("/api/stop");
}

function App() {
  return (
    <>
      <CssBaseline />
      <Button sx={{ width: "50vw", height: "100vh" }} onClick={start}>
        Start
      </Button>
      <Button sx={{ width: "50vw", height: "100vh" }} onClick={stop}>
        Stop
      </Button>
    </>
  );
}

export default App;
