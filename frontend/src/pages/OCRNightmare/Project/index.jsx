import { Link, Outlet, useParams } from 'react-router-dom';
import { useGetProject } from '../../../hooks/useRQHooks';
import ProjData from '../components/ProjData';


const Project = () => {

  let { projName } = useParams();

  const { data:proj_data } = useGetProject(projName, { enabled: !!projName });

  // const { pathname } = useLocation();


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
                  <Link to='extract'>
                    <p>Extract</p>
                  </Link>
                  : <p className="text-gray-400">Extract</p>
              }
              {
                proj_data?.status === 1 ?
                  <Link to='text_lines'>
                    <p>View TextLines</p>
                  </Link>
                  : <p className="text-gray-400">View TextLines</p>
              }
              {
                proj_data?.status === 1 ?
                  <Link to='pages'>
                    <p>View Pages</p>
                  </Link>
                  : <p className="text-gray-400">View Pages</p>
              }
              {
                proj_data?.status === 1 ?
                  <Link to='headers'>
                    <p>Select Headers</p>
                  </Link>
                  : <p className="text-gray-400">Select Headers Pages</p>
              }
            </div>
          </div>
        </div>
      </div>

      <div className="mt-8 text-justify">
        <div className="w-9/12 mx-auto">
          <div className="px-6 py-6 odd:bg-white even:bg-slate-100">
            <Outlet />
          </div>
        </div>
      </div>
    </>
  )
}

export default Project