
<html>


{{infos}}
        List>>>>
         <ul>
          % for info in infos:
             <li>
              {{info['index']}} : <a href={{info['link']}}> {{info['title']}} </a>
             </li>       
             
            <br> 
          % end
         </ul>


</html>