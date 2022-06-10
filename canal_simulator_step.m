function depth_error = canal_simulator_step(u, et, d_ind)    %et ==> depth_error in previous time step
    load Linear_Model_ICSS_opt.mat
    et =et';
    %d=[.200 .300 .200 .300 .200 .300 .200 .300];% turnout demnads

  d=[0.2 0  0  0  0   0  0  0  ];%
 %   d= [1.5 1.5 1.5 0 0 0.1 1 2];
    %d=[1.3 1.2 1.3 0 0 -0.2 0.8 1.7];
   % if d_ind < 500
      % d=[1 2 0.7 0.5 0 0 0 0];
   % elseif d_ind >= 500 && d_ind < 1000
     % d=[0 0 0.1 0.1 0 0 0 0];
   % elseif d_ind >= 1000 && d_ind < 1500
    %  d=[0 0 0 0 0.1 0.1 0 0];
   % else
      % d=[0 0 0 0 0 0 0.2 0.2];
  %  end

    d=d';
    u=u';
    depth_error=A_icss*et+Bu_icss*u+Bd_icss*d;
end