// import { useQuery, useQueries, useMutation, useQueryClient } from 'react-query';
import { useQuery } from 'react-query';
import { APIPoints } from '../helpers/helpers';

const getBasicFetch = async (endPoint) => {
  const response = await fetch(endPoint, {
    headers: {
      Accept: 'application/json',
    },
    credentials: 'include',
    method: 'GET',
    mode: 'cors',
  });
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
};

// const postBasicFetch = async (formData, endPoint, json = false) => {
//   const response = await fetch(endPoint, {
//     headers: json
//       ? {
//           Accept: 'application/json',
//           'Content-Type': 'application/json',
//         }
//       : {
//           Accept: 'application/json',
//         },

//     credentials: 'include',
//     method: 'post',
//     mode: 'cors',
//     body: formData,
//   });
//   if (!response.ok) {
//     throw new Error('Network response was not ok');
//   }
//   return response.json();
// };

// # Project List
const getProjList = async () => {
  const temp = await getBasicFetch(APIPoints.PROJECT);
  return temp.result.projects;
};

export const useGetProjList = () => {
  return useQuery('projList', getProjList);
};

// # Project Data
const getProject = async ({ queryKey }) => {
  // eslint-disable-next-line no-unused-vars
  const [_key, projName] = queryKey;
  const temp = await getBasicFetch(`${APIPoints.PROJECT}/${projName}`);
  console.log('getProject', temp);
  return temp.result.project;
};

export const useGetProject = (projName, conObj) => {
  return useQuery(['project', projName], getProject, conObj);
};

// # TextLines List
const getTextLines = async ({ queryKey }) => {
  // eslint-disable-next-line no-unused-vars
  const [_key, projName] = queryKey;
  const temp = await getBasicFetch(`${APIPoints.PROJECT}/${projName}/text_lines`);

  return temp.result.text_lines;
};

export const useGetTextLines = (projName, conObj) => {
  return useQuery(['textLines', projName], getTextLines, {
    ...conObj,
    refetchOnWindowFocus: false,
  });
};

// # Pages List
const getPages = async ({ queryKey }) => {
  // eslint-disable-next-line no-unused-vars
  const [_key, projName] = queryKey;
  const temp = await getBasicFetch(`${APIPoints.PROJECT}/${projName}/pages`);

  return temp.result.pages;
};

export const useGetPages = (projName, conObj) => {
  return useQuery(['pages', projName], getPages, {
    ...conObj,
    refetchOnWindowFocus: false,
  });
};

// # Page List
const getPage = async ({ queryKey }) => {
  // eslint-disable-next-line no-unused-vars
  const [_key, projName, page_id] = queryKey;
  const temp = await getBasicFetch(`${APIPoints.PROJECT}/${projName}/pages/${page_id}`);

  return temp.result.page;
};

export const useGetPage = (projName, page_id, conObj) => {
  return useQuery(['page', projName, page_id], getPage, {
    ...conObj,
    refetchOnWindowFocus: false,
  });
};

// # Page List
const GetPageWTL = async ({ queryKey }) => {
  // eslint-disable-next-line no-unused-vars
  const [_key, projName, page_id] = queryKey;
  const temp = await getBasicFetch(`${APIPoints.PROJECT}/${projName}/pages/${page_id}/w_tl`);

  return temp.result.page;
};

export const useGetPageWTL = (projName, page_id, conObj) => {
  return useQuery(['page', projName, page_id], GetPageWTL, {
    ...conObj,
    refetchOnWindowFocus: false,
  });
};
