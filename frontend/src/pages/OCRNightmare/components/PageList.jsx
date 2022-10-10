import { Link } from 'react-router-dom'

const PageList = ({page_list}) => {
  return (
    <>
     {page_list && page_list.map((page, idx) => (
       <div className="grid  grid-cols-3 gap-x-10" key={`${idx}name`}>
                <Link to={`${page.id}`}>
                  <p>{page.id}</p>
                </Link>
                <p>{page.project_id}</p>
              </div>
            )

            )}
    </>
  )
}

export default PageList