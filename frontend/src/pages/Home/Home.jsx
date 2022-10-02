import { Link } from 'react-router-dom';

function Home() {
  return (
    <>
      <div className="main ">
        <h1>Home</h1>
        <section>
          <Link to="/">Home</Link>
          <Link to="about">About</Link>
          <Link to="quiz">Quiz</Link>
        </section>
      </div>
    </>
  );
}

export default Home;
