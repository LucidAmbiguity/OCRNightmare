import { useGetProjList } from '../../../hooks/useRQHooks';
import ProjList from '../components/ProjList';


const Projects = () => {

  const { data:proj_list } = useGetProjList();

  return (
    <>
      <div>AvailableProjects</div>
      <div className="mt-8 text-justify">
        <div className="w-9/12 mx-auto">
          <div className="px-6 py-6 odd:bg-white even:bg-slate-100">
            <div className="grid  grid-cols-3 gap-x-10">
              <p>name</p>
              <p>status</p>
              <p>pages</p>
            </div>
            <ProjList proj_list={proj_list}/>
          </div>
        </div>
      </div>
    </>
  )
}

export default Projects