import { useParams } from 'react-router-dom';
import { useGetProject } from '../../../hooks/useRQHooks';
import ProjData from '../components/ProjData';


const Project = () => {

  let { projName } = useParams();

  const { data:proj_data } = useGetProject(projName, { enabled: !!projName });

  // const { pathname } = useLocation();
  const handleClickS0 = () => {
    console.log('Project: handleClick')
  }
  const handleClickS1 = () => {
    console.log('Project: handleClick')
  }


  return (
    <>
      <div>Current Project</div>
      <div className="mt-8 text-justify">
        <div className="w-9/12 mx-auto">
          <div className="px-6 py-6 odd:bg-white even:bg-slate-100">
            <div className="grid  grid-cols-3 gap-x-10">
              <p>name</p>
              <p>status</p>
              <p>pages</p>
            </div>
            {<ProjData proj_data={proj_data}/>}
          </div>
        </div>
      </div>

      <div className="mt-8 text-justify">
        <div className="w-9/12 mx-auto">
          <div className="px-6 py-6 odd:bg-white even:bg-slate-100">
            <div className="grid  grid-cols-3 gap-x-10">
              {
                proj_data?.status === 0 ?
                  <button onClick={handleClickS0}>Extract</button>
                  : <button className="text-gray-400">Extract</button>
              }
              {
                proj_data?.status === 1 ?
                  <button onClick={handleClickS1}>View TextLines</button>
                  : <button className="text-gray-400">View TextLines</button>
              }
            </div>
          </div>
        </div>
      </div>

      <div className="mt-8 text-justify">
        <div className="w-9/12 mx-auto">
          <div className="px-6 py-6 odd:bg-white even:bg-slate-100">
            TEXTLINES
          </div>
        </div>
      </div>
    </>
  )
}

export default Project