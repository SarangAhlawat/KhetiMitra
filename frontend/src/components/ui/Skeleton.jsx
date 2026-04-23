export default function Skeleton({

  height = "h-6",
  width = "w-full"

}) {

  return (

    <div

      className={`
        ${height}
        ${width}
        bg-gray-200
        animate-pulse
        rounded
      `}

    />

  );

}